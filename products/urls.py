from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("search/", views.search, name="search"),
    path("categories/", views.category_list, name="category_list"),
    path("categories/<slug:slug>/", views.category_details, name="category_details"),
    path("subcategories/", views.subcategory_list, name="subcategory_list"),
    path("subcategories/<slug:slug>/", views.subcategory_details, name="subcategory_details"),
    # product center static pages
    path("center/<str:page_name>/", views.center_page_view, name="center_page"),
    # catch bare "product/" path and show friendly message instead of 404
    path("product/", views.product_missing, name="product_missing"),
    path("product/<slug:slug>/", views.product_details, name="product_details"),
    path("quote-request/", views.quote_request, name="quote_request"),
    path("catalog-request/", views.catalog_request, name="catalog_request"),
]
