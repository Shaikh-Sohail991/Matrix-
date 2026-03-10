from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-of-service/', views.terms_of_service, name='terms_of_service'),
    path('cookie-policy/', views.cookie_policy, name='cookie_policy'),
    path('faqs/', views.faq, name='faq'),
    path('videos/', views.videos, name='videos'),
    
    # Form submission endpoints
    path('api/newsletter-subscribe/', views.newsletter_subscribe, name='newsletter_subscribe'),
    path('api/contact-submit/', views.contact_submit, name='contact_submit'),
    path('api/service-inquiry/', views.service_inquiry_submit, name='service_inquiry'),
]
