from django.contrib import admin
from django.utils.html import format_html

from .models import Category, Subcategory, Product, ProductImage, Spec, Feature, Quote, CatalogRequest


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name", "slug")
    search_fields = ("name",)
    fields = ("name", "slug", "short_description", "description", "image")


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name", "category", "slug")
    list_filter = ("category",)
    search_fields = ("name",)
    fields = ("category", "name", "slug", "short_description", "description", "image")


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class SpecInline(admin.TabularInline):
    model = Spec
    extra = 1
    fields = ("label", "value")


class FeatureInline(admin.TabularInline):
    model = Feature
    extra = 1
    fields = ("title", "description")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name", "get_subcategory_display", "is_featured", "is_new")
    list_filter = ("subcategory", "is_featured", "is_new")
    search_fields = ("name", "slug")
    inlines = [ProductImageInline, SpecInline, FeatureInline]

    def get_subcategory_display(self, obj):
        """Display subcategory or 'Standalone' if no subcategory."""
        return obj.subcategory if obj.subcategory else "Standalone"
    get_subcategory_display.short_description = "Subcategory"


@admin.register(Spec)
class SpecAdmin(admin.ModelAdmin):
    list_display = ("product", "label", "value")
    list_filter = ("product",)
    search_fields = ("label", "value", "product__name")
    ordering = ("product",)


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ("product", "title")
    list_filter = ("product",)
    search_fields = ("title", "product__name")
    ordering = ("product",)


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email_display", "product_name", "phone_number", "status_badge", "created_at_display")
    list_filter = ("is_read", "created_at", "product_name")
    search_fields = ("full_name", "email", "product_name", "message", "phone_number")
    readonly_fields = ("created_at", "formatted_message")
    
    fieldsets = (
        ("Quote Information", {
            "fields": ("product_name", "created_at")
        }),
        ("Customer Details", {
            "fields": ("full_name", "email", "phone_number")
        }),
        ("Message", {
            "fields": ("formatted_message",)
        }),
        ("Status", {
            "fields": ("is_read",)
        }),
    )
    
    ordering = ("-created_at",)
    actions = ["mark_as_read", "mark_as_unread"]

    def email_display(self, obj):
        """Display email as a clickable link"""
        return format_html('<a href="mailto:{}">{}</a>', obj.email, obj.email)
    email_display.short_description = "Email"

    def status_badge(self, obj):
        """Display status as a colored badge"""
        if obj.is_read:
            color = "#28a745"  # Green
            status = "Read"
        else:
            color = "#ffc107"  # Yellow
            status = "Unread"
        return format_html(
            '<span style="background-color: {}; color: white; padding: 3px 10px; border-radius: 3px; font-weight: bold;">{}</span>',
            color,
            status
        )
    status_badge.short_description = "Status"

    def created_at_display(self, obj):
        """Format the creation date"""
        return obj.created_at.strftime("%b %d, %Y %I:%M %p")
    created_at_display.short_description = "Received On"

    def formatted_message(self, obj):
        """Display message in a readable format"""
        return format_html('<p style="white-space: pre-wrap;">{}</p>', obj.message)
    formatted_message.short_description = "Message"

    @admin.action(description="Mark selected quotes as read")
    def mark_as_read(self, request, queryset):
        updated = queryset.update(is_read=True)
        self.message_user(request, f"{updated} quote(s) marked as read.")

    @admin.action(description="Mark selected quotes as unread")
    def mark_as_unread(self, request, queryset):
        updated = queryset.update(is_read=False)
        self.message_user(request, f"{updated} quote(s) marked as unread.")

    def has_add_permission(self, request):
        return False


@admin.register(CatalogRequest)
class CatalogRequestAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email_display", "product_name", "phone_number", "status_badge", "created_at_display")
    list_filter = ("is_read", "created_at", "product_name")
    search_fields = ("full_name", "email", "product_name", "phone_number")
    readonly_fields = ("product_name", "full_name", "email", "phone_number", "created_at")

    fieldsets = (
        ("Request Information", {
            "fields": ("product_name", "created_at")
        }),
        ("Customer Details", {
            "fields": ("full_name", "email", "phone_number")
        }),
        ("Status", {
            "fields": ("is_read",)
        }),
    )

    ordering = ("-created_at",)
    actions = ["mark_as_read", "mark_as_unread"]

    def email_display(self, obj):
        return format_html('<a href="mailto:{email}">{email}</a>', email=obj.email)
    email_display.short_description = "Email"

    def status_badge(self, obj):
        if obj.is_read:
            color, status = "#28a745", "Read"
        else:
            color, status = "#ffc107", "Unread"
        return format_html(
            '<span style="background-color:{};color:white;padding:3px 10px;border-radius:3px;font-weight:bold;">{}</span>',
            color, status,
        )
    status_badge.short_description = "Status"

    def created_at_display(self, obj):
        return obj.created_at.strftime("%b %d, %Y %I:%M %p")
    created_at_display.short_description = "Received On"

    @admin.action(description="Mark selected requests as read")
    def mark_as_read(self, request, queryset):
        updated = queryset.update(is_read=True)
        self.message_user(request, f"{updated} request(s) marked as read.")

    @admin.action(description="Mark selected requests as unread")
    def mark_as_unread(self, request, queryset):
        updated = queryset.update(is_read=False)
        self.message_user(request, f"{updated} request(s) marked as unread.")

    def has_add_permission(self, request):
        return False
