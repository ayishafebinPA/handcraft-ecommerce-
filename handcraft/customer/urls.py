from django.urls import path
from .views import customerhomeview,addcart,cartshowview,cartdeleteview,checkoutview,ordershow,edit_profile

urlpatterns = [
    path('customerhome',customerhomeview.as_view(),name='home'),
    path('addcart/<int:pid>',addcart.as_view(),name='addcart'),
    path('carttshow',cartshowview.as_view(),name='cartshow'),
    path('cartdelete/<int:id>',cartdeleteview,name='delcart'),
    path('checkoutt/<int:cid>',checkoutview.as_view(),name="ckout"),
    path('orders',ordershow.as_view(),name='ordershoww'),
    path('profile/edit/',edit_profile, name='edit_profile'),

]