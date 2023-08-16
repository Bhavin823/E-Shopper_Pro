from django.shortcuts import render
from category_app.views import CategoryView,Cat_Subcat_Nav_View

# Create your views here.
def baseview(request):
    return render(request,'base_app/base.html')

def homeview(request):
    categories = CategoryView()
    cat_subcat_for_nav = Cat_Subcat_Nav_View()
    # print("categories",categories)
    context = {
        'categories': categories,
        'cat_sub_nav' : cat_subcat_for_nav
    }
    return render(request,'base_app/home.html',context)

