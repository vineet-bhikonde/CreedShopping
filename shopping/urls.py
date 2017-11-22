from django.conf.urls import url
from django.contrib import admin
from products import views as product_views
from cart import views as cart_views
from users import views as users_views

urlpatterns = [

    url(r'^admin/', admin.site.urls),

    url(r'^$',product_views.home,name='home'),

    url(r'^about/$',product_views.about,name='about'),

    url(r'^contact/$',product_views.contact,name='contact'),

    url(r'^cart/(?P<product_id>\w+)/$',cart_views.cart_view,name='cart_view'),

    url(r'^cart/$',cart_views.cart,name='cart'),

    url(r'^thanks/$',product_views.thanks,name='thanks'),
    
    url(r'^signup/$',users_views.SignUp,name='signup'),

    url(r'^signin/$',users_views.SignIn,name='signin'),

    url(r'^mobile/$',product_views.mobile_details,name='mobile'),

    url(r'^stationary/$',product_views.stationary_details,name='stationary'),

    url(r'^logout/$',users_views.Logout,name='logout'),

    url(r'^cart/checkout/$',cart_views.checkout,name='checkout'),

    url(r'^cart/\d{1,5}/checkout/$',cart_views.checkout,name='checkout'),

    url(r'^orders/$',users_views.Orders,name='orders'),

]