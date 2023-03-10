from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from django.contrib.auth import views as auth_views
from django.urls import path, include
from order.views import admin_order_pdf
from userprofile.views import  myaccount, profile, seller_profile, signup
from core.views import ItemDetailView,about, CheckoutView, SearchResultsView, HomeView, add_to_cart, remove_from_cart, OrderSummaryView, remove_single_item_from_cart, contact_view,  PaymentView, final_checkout, addproducts, delete_product, my_listings,ProductUpdateView
#search_products,
from dispatch import receiver
# from django.views.decorators.csrf import csrf_exempt
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home_page'),
    path('add/', addproducts, name='addProducts'),
    path('mylistings/', my_listings,name='mylistings'),
    path('delete/<int:id>/', delete_product,name='delete_product'),
    path('update/<int:pk>/',ProductUpdateView.as_view(),name='update_product'),
    path('contact/', contact_view, name='contact'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('about/', about, name='about'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('add-to-cart/<slug>', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>', remove_from_cart, name='remove-from-cart'),
    path('products/<slug>/', ItemDetailView.as_view(), name='product_page'),
    path('order-summary', OrderSummaryView.as_view(), name='order_summary'),
    path('remove-single-item-from-cart/<slug>', remove_single_item_from_cart, name='remove_single_item_from_cart'),
    path('accounts/', include('allauth.urls')),
    path('profile/', profile, name='profile'),
    path('sellerprofile/<int:id>/',seller_profile,name='sellerprofile'),
    path('myaccount/', myaccount, name='myaccount'),
    path('signup/', signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('verify/<int:id>', PaymentView.as_view(), name='verify_payment'),
    path('final-checkout/', final_checkout, name='f_checkout'),
    path('admin_order_pdf/<int:order_id>/', admin_order_pdf, name='admin_order_pdf'),
    # path('search-products/', csrf_exempt(search_products), name='search-products'),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
