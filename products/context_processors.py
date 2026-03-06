from .models import Category


def nav_categories(request):
    """Inject all categories into every template context for navbar/footer."""
    return {
        "nav_categories": Category.objects.all(),
    }
