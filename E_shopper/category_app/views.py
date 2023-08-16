from django.shortcuts import render
from category_app.models import *

# Create your views here.
def Cat_Subcat_Nav_View():
    categories= CategoryModel.objects.all()
    
    categoryHeader=[]
    for category in categories:
        subcategories=SubCategoryModel.objects.filter(category=category.pk)
        
        subcategoryArray=[]
        for subcategory in subcategories:
            subcategoryDict = {"subId:":subcategory.pk,"subName":subcategory.subcategoryName}
            subcategoryArray.append(subcategoryDict)
            # print(subcategorydataArray)
        
        categoryDict={"cat_Id":category.pk,"catName":category.categoryName,"subcategory":subcategoryArray}
        
        categoryHeader.append(categoryDict)
    # print("category list:",categoryHeader)

    return categoryHeader

def CategoryView():

    categories = CategoryModel.objects.all()
    
    # print("category from category_app:",)
    return categories

