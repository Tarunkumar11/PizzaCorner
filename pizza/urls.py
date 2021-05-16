from django.conf.urls import url
from .views import HomeView,Menushow,BestdealView

app_name = "pizza"

urlpatterns = [
    url('^$',HomeView,name='home'),
    url('^order/$',Menushow.as_view(),name='order'),
    url('^order/deal/$',BestdealView.as_view(),name='deals_order'),

]