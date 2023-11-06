from django.contrib import admin
from .models import Category, Product

# Register your models here.

@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'quantity']
    ordering = ['category', '-quantity']
    list_filter = ['date_added', 'price', 'category']
    search_fields = ['description']
    search_help_text = 'Поиск по полю описание продукта (description)'
    actions = [reset_quantity]

    """Отдельный продукт."""
    # fields = ['name', 'description', 'category', 'date_added', 'rating'] # отображаемые поля 
    readonly_fields = ['date_added', 'rating'] # поля, доступные только для просмотра 

    # не может одновременно работать с fields *(выше), либо fields-fieldsets
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Категория товара и его подробное описание',
                'fields': ['category', 'description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'quantity'],
            }
        ),
        (
            'Рейтинг и прочее',
            {
                'description': 'Рейтинг сформирован автоматически на основе оценок покупателей',
                'fields': ['rating', 'date_added'],
            }
        ),
    ]



admin.site.register(Category)
admin.site.register(Product, ProductAdmin)

