from django.contrib import admin
from .models import Newsletter, ContactSubmission, ServiceInquiry


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'subscribed_at')
    list_filter = ('is_active', 'subscribed_at')
    search_fields = ('email',)
    readonly_fields = ('subscribed_at',)
    date_hierarchy = 'subscribed_at'


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'subject', 'is_read', 'submitted_at')
    list_filter = ('is_read', 'subject', 'submitted_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    readonly_fields = ('submitted_at',)
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone')
        }),
        ('Message', {
            'fields': ('subject', 'message')
        }),
        ('Status', {
            'fields': ('is_read', 'agree_terms', 'submitted_at')
        }),
    )
    date_hierarchy = 'submitted_at'
    actions = ['mark_as_read', 'mark_as_unread']

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected as read"

    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
    mark_as_unread.short_description = "Mark selected as unread"


@admin.register(ServiceInquiry)
class ServiceInquiryAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'email', 'service_name', 'is_read', 'submitted_at')
    list_filter = ('is_read', 'service_name', 'submitted_at')
    search_fields = ('customer_name', 'email', 'phone')
    readonly_fields = ('submitted_at',)
    fieldsets = (
        ('Customer Information', {
            'fields': ('customer_name', 'email', 'phone')
        }),
        ('Service', {
            'fields': ('service_name', 'message')
        }),
        ('Status', {
            'fields': ('is_read', 'submitted_at')
        }),
    )
    date_hierarchy = 'submitted_at'
    actions = ['mark_as_read', 'mark_as_unread']

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected as read"

    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
    mark_as_unread.short_description = "Mark selected as unread"
