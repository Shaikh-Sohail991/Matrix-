from collections import defaultdict
from urllib.parse import urlencode

from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from .models import Category, Subcategory, Product, Quote, CatalogRequest, Spec


# ---------------------------------------------------------------------------
# Helper: build sidebar filter options + resolve selected GET params
# ---------------------------------------------------------------------------

def _build_spec_filters(spec_qs, request_get):
    """Return (filters, active_filters, filter_query_string).

    filters               – list of {name, options} dicts for the sidebar template
    active_filters        – dict of {real_label: [selected_values]} for ORM filtering
    filter_query_string   – URL-encoded string of current filter params (no 'page')
    """
    spec_data = (
        spec_qs
        .values("label", "value")
        .annotate(count=Count("product", distinct=True))
        .order_by("label", "value")
    )

    slug_to_label = {}   # 'spec_voltage' → 'Voltage'
    filters_dict = defaultdict(list)

    for item in spec_data:
        slug_key = "spec_" + item["label"].replace(" ", "_").lower()
        slug_to_label[slug_key] = item["label"]
        opt_id = slug_key + "_" + item["value"].replace(" ", "_").replace("/", "-").lower()
        filters_dict[item["label"]].append({
            "id": opt_id,
            "name": slug_key,       # HTML input name
            "label": item["value"], # Display text AND the submitted value
            "count": item["count"],
            "checked": False,       # filled in below
        })

    # Resolve which values are currently selected
    active_filters = {}  # real_label → [values]
    for slug_key, real_label in slug_to_label.items():
        values = [v for v in request_get.getlist(slug_key) if v]
        if values:
            active_filters[real_label] = values

    # Mark checked options
    for real_label, opts in filters_dict.items():
        selected_vals = active_filters.get(real_label, [])
        for opt in opts:
            opt["checked"] = opt["label"] in selected_vals

    filters = [{"name": label, "options": opts} for label, opts in filters_dict.items()]

    # Build query string preserving only spec_ params (not page)
    params = []
    for slug_key in slug_to_label:
        for v in request_get.getlist(slug_key):
            if v:
                params.append((slug_key, v))
    filter_query_string = urlencode(params)

    return filters, active_filters, filter_query_string


# --- category related -----------------------------------------------------

def category_list(request):
    """Display a page listing every category."""
    categories = Category.objects.all()
    # counts are exposed as properties so templates can read them directly
    return render(request, "category.html", {"categories": categories})


def category_details(request, slug):
    category = get_object_or_404(Category, slug=slug)

    # Build spec filters from all products in this category
    spec_qs = Spec.objects.filter(product__subcategory__category=category)
    filters, active_filters, filter_query_string = _build_spec_filters(spec_qs, request.GET)

    # Featured products, with optional spec filtering
    featured = Product.objects.filter(subcategory__category=category, is_featured=True)
    for label, values in active_filters.items():
        featured = featured.filter(specs__label=label, specs__value__in=values).distinct()

    return render(
        request,
        "category_details.html",
        {
            "category": category,
            "featured": featured,
            "filters": filters,
            "filter_query_string": filter_query_string,
            "active_filter_count": sum(len(v) for v in active_filters.values()),
        },
    )


# --- subcategory -----------------------------------------------------------

def subcategory_list(request):
    """Display a page listing every subcategory grouped by category."""
    categories = Category.objects.prefetch_related("subcategories").all()
    # Build a list of dicts so the template can iterate cleanly
    grouped = [
        {
            "name": cat.name,
            "slug": cat.slug,
            "subcategories": list(cat.subcategories.all()),
        }
        for cat in categories
    ]
    return render(request, "subcategory.html", {"categories": grouped})


def subcategory_details(request, slug):
    subcategory = get_object_or_404(Subcategory, slug=slug)

    # Build spec filters for this subcategory
    spec_qs = Spec.objects.filter(product__subcategory=subcategory)
    filters, active_filters, filter_query_string = _build_spec_filters(spec_qs, request.GET)

    # Products, with optional spec filtering applied
    products_qs = subcategory.products.all()
    for label, values in active_filters.items():
        products_qs = products_qs.filter(specs__label=label, specs__value__in=values).distinct()

    paginator = Paginator(products_qs, 20)
    page_obj = paginator.get_page(request.GET.get("page"))

    return render(
        request,
        "subcategory_details.html",
        {
            "subcategory": subcategory,
            "page_obj": page_obj,
            "filters": filters,
            "filter_query_string": filter_query_string,
            "active_filter_count": sum(len(v) for v in active_filters.values()),
        },
    )


# --- products --------------------------------------------------------------

def product_list(request):
    query = Product.objects.select_related("subcategory", "subcategory__category").all()
    category_slug = request.GET.get("category")
    if category_slug:
        query = query.filter(subcategory__category__slug=category_slug)

    # Build spec filters scoped to the current queryset
    spec_qs = Spec.objects.filter(product__in=query)
    filters, active_filters, filter_query_string = _build_spec_filters(spec_qs, request.GET)

    # Apply spec filters
    for label, values in active_filters.items():
        query = query.filter(specs__label=label, specs__value__in=values).distinct()

    paginator = Paginator(query, 20)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(
        request,
        "products.html",
        {
            "page_obj": page_obj,
            "filters": filters,
            "filter_query_string": filter_query_string,
            "active_filter_count": sum(len(v) for v in active_filters.values()),
        },
    )


def product_missing(request):
    """User navigated to /products/product/ without specifying a slug.

    Rather than a generic 404, show a friendly page encouraging them to
    choose a product (with a link to the full product list).
    """
    return render(
        request,
        "product_missing.html",
        {"message": "It looks like you haven't selected a product yet."},
    )


def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug)
    # Get related products from same subcategory, or get featured products if standalone
    if product.subcategory:
        related_products = (
            Product.objects.filter(subcategory=product.subcategory)
            .exclude(pk=product.pk)
            [:4]
        )
    else:
        # For standalone products, show featured products as related
        related_products = (
            Product.objects.filter(is_featured=True)
            .exclude(pk=product.pk)
            [:4]
        )
    support = {
        "phone": "1-800-000-000",
        "label_call": "Call Us",
        "label_email": "Email Us",
    }
    related_services = [
        {"name": "Manufacturing",                 "icon": "bi-gear-wide-connected"},
        {"name": "Sales & Distribution",          "icon": "bi-box-seam"},
        {"name": "Installation & Commissioning",  "icon": "bi-tools"},
        {"name": "Calibration & Testing",         "icon": "bi-speedometer2"},
        {"name": "Repair & Maintenance",          "icon": "bi-wrench-adjustable"},
        {"name": "Annual Maintenance Contracts",  "icon": "bi-calendar-check"},
        {"name": "Custom Equipment Development",  "icon": "bi-lightbulb"},
    ]

    return render(
        request,
        "product_details.html",
        {
            "product": product,
            "related_products": related_products,
            "support": support,
            "related_services": related_services,
        },
    )


@require_http_methods(["POST"])
def catalog_request(request):
    """Handle catalog / documentation request form."""
    try:
        product_name = request.POST.get("productName", "").strip()
        full_name = request.POST.get("fullName", "").strip()
        email = request.POST.get("email", "").strip()
        phone_number = request.POST.get("phoneNumber", "").strip()

        if not all([product_name, full_name, email, phone_number]):
            return JsonResponse(
                {"success": False, "message": "All fields are required."},
                status=400,
            )

        CatalogRequest.objects.create(
            product_name=product_name,
            full_name=full_name,
            email=email,
            phone_number=phone_number,
        )

        return JsonResponse(
            {"success": True, "message": "Request submitted! Your documentation will now open."}
        )
    except Exception as e:
        return JsonResponse(
            {"success": False, "message": f"An error occurred: {str(e)}"},
            status=500,
        )


@require_http_methods(["POST"])
def quote_request(request):
    """Handle quote request submission from product details page."""
    try:
        product_name = request.POST.get("productName", "").strip()
        full_name = request.POST.get("fullName", "").strip()
        email = request.POST.get("email", "").strip()
        phone_number = request.POST.get("phoneNumber", "").strip()
        message = request.POST.get("message", "").strip()

        # Validation
        if not all([product_name, full_name, email, phone_number, message]):
            return JsonResponse(
                {"success": False, "message": "All fields are required."},
                status=400,
            )

        # Create quote request
        Quote.objects.create(
            product_name=product_name,
            full_name=full_name,
            email=email,
            phone_number=phone_number,
            message=message,
        )

        return JsonResponse(
            {
                "success": True,
                "message": "Your quote request has been submitted successfully! We will contact you soon.",
            }
        )
    except Exception as e:
        return JsonResponse(
            {"success": False, "message": f"An error occurred: {str(e)}"},
            status=500,
        )


# --- search ----------------------------------------------------------------

def search(request):
    """Search across Category, Subcategory, and Product by name / description."""
    from django.db import models as db_models
    query = request.GET.get("q", "").strip()

    categories = Category.objects.none()
    subcategories = Subcategory.objects.none()
    products = Product.objects.none()

    if query:
        categories = Category.objects.filter(
            db_models.Q(name__icontains=query) | db_models.Q(short_description__icontains=query)
        )
        subcategories = Subcategory.objects.select_related("category").filter(
            db_models.Q(name__icontains=query) | db_models.Q(short_description__icontains=query)
        )
        products = (
            Product.objects.select_related("subcategory", "subcategory__category")
            .filter(
                db_models.Q(name__icontains=query)
                | db_models.Q(short_description__icontains=query)
                | db_models.Q(description__icontains=query)
            )
        )

    total = (
        (categories.count() if query else 0)
        + (subcategories.count() if query else 0)
        + (products.count() if query else 0)
    )

    return render(
        request,
        "search.html",
        {
            "query": query,
            "categories": categories,
            "subcategories": subcategories,
            "products": products,
            "total": total,
        },
    )
