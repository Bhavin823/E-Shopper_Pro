from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify
from category_app.models import CategoryModel, SubCategoryModel

class Command(BaseCommand):
    help = 'Fixes duplicate subcategory slugs within the same category'

    def handle(self, *args, **options):
        subcategories = SubCategoryModel.objects.all()

        for subcategory in subcategories:
            category_slug = slugify(subcategory.category.categoryName)
            subcategory_slug = slugify(subcategory.subcategoryName)
            combined_slug = f"{category_slug}-{subcategory_slug}"

            # Check for existing subcategory slugs and increment counter if necessary
            counter = 1
            while SubCategoryModel.objects.filter(slug=combined_slug).exclude(id=subcategory.id).exists():
                combined_slug = f"{category_slug}-{subcategory_slug}-{counter}"
                counter += 1

            subcategory.slug = combined_slug
            subcategory.save()
