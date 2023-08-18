from django.db import models
from django.utils.text import slugify
from category_app.models import CategoryModel,SubCategoryModel

# Create your models here.


class ProductModel(models.Model):
    ProductName = models.CharField(max_length=100)
    ProductImage = models.ImageField(blank=True,upload_to='product/')
    category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategoryModel,on_delete=models.CASCADE)
    brandName = models.CharField(max_length=100)
    ProductPrice =models.IntegerField()
    sellerName = models.CharField(max_length=100)
    ProductDetail = models.TextField()

    slug = models.SlugField(unique=True, max_length=100, blank=True, editable=False)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.ProductName)  # Generate slug from product name
        super(ProductModel, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.ProductName
    
