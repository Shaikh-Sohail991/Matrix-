from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from .models import Newsletter, ContactSubmission, ServiceInquiry

from products.models import Product
import random
from datetime import date


def get_daily_products(count=6):
    """Return a pseudo-random but stable set of products which changes daily."""
    qs = list(Product.objects.all())
    if not qs:
        return []
    # deterministic shuffle based on current day
    seed = date.today().toordinal()
    rand = random.Random(seed)
    rand.shuffle(qs)
    return qs[:count]


def index(request):
    # hero product remains the first featured item
    hero_product = Product.objects.filter(is_featured=True).first()
    # pick six products that rotate every day
    daily_products = get_daily_products(6)
    # company customers for logos section
    from .models import Customer
    customers = Customer.objects.all()[:12]
    return render(request, 'index.html', {'hero_product': hero_product, 'daily_products': daily_products, 'customers': customers})

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def terms_of_service(request):
    return render(request, 'terms_of_service.html')

def cookie_policy(request):
    return render(request, 'cookie_policy.html')


def faq(request):
    # static FAQ content rendered from template
    return render(request, 'faq.html')

def videos(request):
    from .models import YouTubeVideo
    from django.db.models import Count

    videos = YouTubeVideo.objects.all()
    # compute counts by category for use in the UI
    counts_qs = YouTubeVideo.objects.values('category').annotate(count=Count('id'))
    category_counts = {item['category']: item['count'] for item in counts_qs}

    return render(request, 'video.html', {
        'videos': videos,
        'category_counts': category_counts,
        'category_choices': YouTubeVideo.CATEGORY_CHOICES,
    })


@require_http_methods(["POST"])
def newsletter_subscribe(request):
    """Handle newsletter subscription"""
    email = request.POST.get('email', '').strip()
    
    if not email:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'message': 'Email is required.'})
        messages.error(request, 'Email is required.')
        return redirect(request.META.get('HTTP_REFERER', '/'))
    
    try:
        newsletter, created = Newsletter.objects.get_or_create(email=email)
        if created:
            message_text = 'Thank you! You have been subscribed to our newsletter.'
        else:
            message_text = 'This email is already subscribed.'
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': True, 'message': message_text})
        messages.success(request, message_text)
    except Exception as e:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'message': 'An error occurred. Please try again.'})
        messages.error(request, 'An error occurred. Please try again.')
    
    return redirect(request.META.get('HTTP_REFERER', '/'))


@require_http_methods(["POST"])
def contact_submit(request):
    """Handle contact form submission"""
    first_name = request.POST.get('firstName', '').strip()
    last_name = request.POST.get('lastName', '').strip()
    email = request.POST.get('email', '').strip()
    phone = request.POST.get('phone', '').strip()
    subject = request.POST.get('subject', '').strip()
    message = request.POST.get('message', '').strip()
    agree_terms = request.POST.get('termsCheck') == 'on'
    
    # Validate required fields
    if not all([first_name, last_name, email, phone, message, agree_terms]):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'message': 'All required fields must be filled.'})
        messages.error(request, 'All required fields must be filled.')
        return redirect(request.META.get('HTTP_REFERER', '/'))
    
    try:
        ContactSubmission.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            subject=subject or 'general',
            message=message,
            agree_terms=agree_terms
        )
        message_text = 'Thank you! Your message has been received. We will get back to you within 24 hours.'
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': True, 'message': message_text})
        messages.success(request, message_text)
    except Exception as e:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'message': 'An error occurred. Please try again.'})
        messages.error(request, 'An error occurred. Please try again.')
    
    return redirect(request.META.get('HTTP_REFERER', '/'))


@require_http_methods(["POST"])
def service_inquiry_submit(request):
    """Handle service inquiry form submission"""
    service_name = request.POST.get('service', '').strip()
    customer_name = request.POST.get('customerName', '').strip()
    email = request.POST.get('email', '').strip()
    phone = request.POST.get('phone', '').strip()
    message = request.POST.get('message', '').strip()
    
    # Validate required fields
    if not all([service_name, customer_name, email, phone]):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'message': 'All required fields must be filled.'})
        messages.error(request, 'All required fields must be filled.')
        return redirect(request.META.get('HTTP_REFERER', '/'))
    
    try:
        ServiceInquiry.objects.create(
            service_name=service_name,
            customer_name=customer_name,
            email=email,
            phone=phone,
            message=message or ''
        )
        message_text = 'Thank you! Your service inquiry has been submitted. Our team will contact you soon.'
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': True, 'message': message_text})
        messages.success(request, message_text)
    except Exception as e:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'message': 'An error occurred. Please try again.'})
        messages.error(request, 'An error occurred. Please try again.')
    
    return redirect(request.META.get('HTTP_REFERER', '/'))
