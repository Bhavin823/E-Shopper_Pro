from django.shortcuts import render,get_object_or_404
from product_app.models import ProductModel
from category_app.models import SubCategoryModel
from category_app.views import Cat_Subcat_Nav_View
from cart_app.models import CartModel

# Create your views here.
def ProductView(request,subcatslug):
    if subcatslug == 'all':
        products = ProductModel.objects.all() # fetch all products
        subcateheadername = "All Products" # Set subcategory name to "All Products"
    else:
        subcategoryslug = get_object_or_404(SubCategoryModel, slug=subcatslug) #fetch slug of specified product
        products  = ProductModel.objects.filter(subcategory=subcategoryslug) #fetcg those product which subcategort match
        subcateheadername = subcategoryslug.subcategoryName # Get the name of the subcategory
    
    cat_subcat_for_nav = Cat_Subcat_Nav_View()  # left sidebar 
    # print("products:",products)

    if request.user.is_authenticated:
        for product in products:
            product.quantity_in_cart = 0  # Default value if not in cart
            for item in request.user.cartmodel.items.all():
                if item.product == product:
                    product.quantity_in_cart = item.quantity
    
    context = {
        'cat_sub_nav' : cat_subcat_for_nav,
        'subcateheadername':subcateheadername,
        'products' : products,
        'subcatslug':subcatslug
    }
    return render(request,'product_app/product.html',context)

def ProductDetailView(request,productslug):
    productdetail = ProductModel.objects.get(slug=productslug)  # fetch productdetail
    # print(productdetail)
    
    cat_subcat_for_nav = Cat_Subcat_Nav_View() #left sidebar
    
    if request.user.is_authenticated:
        productdetail.quantity_in_cart = 0
        for item in request.user.cartmodel.items.all():
            # print("item:",item)
            if item.product == productdetail:
                # print(f"product item= {item.product} == productdetal {productdetail}")
                productdetail.quantity_in_cart = item.quantity
                # print(f"item's quantity = {item.quantity}")
                

    
    context = {
        'cat_sub_nav' : cat_subcat_for_nav,
        'productdetail': productdetail,
    }
    return render(request,'product_app/productdetail.html',context)
