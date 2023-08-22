from django.shortcuts import render,get_object_or_404
from product_app.models import ProductModel
from category_app.models import SubCategoryModel
from category_app.views import Cat_Subcat_Nav_View

# Create your views here.
def ProductView(request,productslug):
    if productslug == 'all':
        products = ProductModel.objects.all() # fetch all products
        subcateheadername = "All Products" # Set subcategory name to "All Products"
    else:
        subcategoryslug = get_object_or_404(SubCategoryModel, slug=productslug) #fetch slug of specified product
        products  = ProductModel.objects.filter(subcategory=subcategoryslug) #fetcg those product which subcategort match
        subcateheadername = subcategoryslug.subcategoryName # Get the name of the subcategory
    
    cat_subcat_for_nav = Cat_Subcat_Nav_View()  # left sidebar 
    print("products:",products)
    
    context = {
        'cat_sub_nav' : cat_subcat_for_nav,
        'subcateheadername':subcateheadername,
        'products' : products,
    }
    return render(request,'product_app/product.html',context)

def ProductDetailView(request,productdetailslug):
    productdetail = ProductModel.objects.get(slug=productdetailslug)  # fetch productdetail
    # print(productdetail)
    cat_subcat_for_nav = Cat_Subcat_Nav_View() #left sidebar
    context = {
        'cat_sub_nav' : cat_subcat_for_nav,
        'productdetail': productdetail,
    }
    return render(request,'product_app/productdetail.html',context)
