from django.urls import path
from . import views
from .forms import LoginForm,UserPasswordChangeForm,UserPasswordResetForm,UserSetPasswordForm
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.HomeProductListView.as_view(), name='index'),

    #URLs for Products
    path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('mobile/<slug:data>/', views.MobileListView.as_view(), name='mobile'),
    path('laptop/<slug:data>/', views.LaptopListView.as_view(), name='laptop'),
    path('topwear/<slug:data>/', views.TopWearListView.as_view(), name='topwear'),
    path('bottomwear/<slug:data>/', views.BottomWearListView.as_view(), name='bottomwear'),
    #URLs for displaying data
    path('address/', views.AddressListView.as_view(), name='address'),
    #path('changepassword/', views.change_password, name='changepassword'),
   
    path('displaycart/',views.displayCart,name="display_cart"),


    #URLs related to checkout and payment
    path('add-to-cart/', views.addToCart, name='add-to-cart'),
    path('cart/', views.ShowCartView.as_view(), name='show_cart'),
    path('payment/', views.payment, name='payment'),
    path('orders/', views.OrderPlacedListView.as_view(), name='orders'),
    path('checkout/', views.checkout, name='checkout'),
    path('buy-now/<int:pk>', views.buyNow, name='buy_now'),


    path('plcart/<slug:operator>', views.alterCart, name='pl_cart'),
    path('mncart/<slug:operator>', views.alterCart, name='mn_cart'),
    path('removecart/<slug:operator>', views.alterCart, name='rm_cart'),


   
    # URLs Related to account. Will also make sapparate app.
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm
    ), name='login'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name='app/changepassword.html',form_class=UserPasswordChangeForm
    ), name='changepassword'),
     path('changepassword/done/', auth_views.PasswordChangeDoneView.as_view(template_name='app/changepassworddone.html'
    ), name='password_change_done'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='app/resetpassword.html',form_class=UserPasswordResetForm), name='password_reset'),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='app/resetpassworddone.html'), name='password_reset_done'),
    path('reset-password-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='app/resetpasswordconfirm.html', form_class=UserSetPasswordForm), name='password_reset_confirm'),
    path('reset-password-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='app/resetpasswordcomplete.html', ), name='password_reset_complete'),


    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),

    
]
