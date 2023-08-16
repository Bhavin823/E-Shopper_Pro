from django.contrib import admin
from category_app.models import CategoryModel,SubCategoryModel

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['categoryName',]

@admin.register(SubCategoryModel)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['subcategoryName','category',]
    list_filter = ['category',]