from django.shortcuts import render
from product_app.models import ProductModel
from category_app.models import SubCategoryModel
from category_app.views import Cat_Subcat_Nav_View

# Create your views here.
def ProductView(request,productslug):
    subcategoryslug = SubCategoryModel.objects.get(slug=productslug)
    products  = ProductModel.objects.filter(subcategory=subcategoryslug)
    cat_subcat_for_nav = Cat_Subcat_Nav_View()
    print(products[0].subcategory)
    print("products:",products)
    context = {
        'cat_sub_nav' : cat_subcat_for_nav,
        'products' : products
    }
    return render(request,'product_app/product.html',context)
