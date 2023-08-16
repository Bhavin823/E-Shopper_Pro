from django.db import models

# Create your models here.
# image validation

class CategoryModel(models.Model):
    categoryName = models.CharField(max_length=100,unique=True)
    categoryImage = models.ImageField(upload_to='category',blank=True,)

    def __str__(self) -> str:
        return self.categoryName

class SubCategoryModel(models.Model):
    subcategoryName= models.CharField(max_length=100)
    category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE)
    subcategoryImage = models.ImageField(upload_to='subcategory',blank=True,)

    def __str__(self) -> str:
        return self.subcategoryName