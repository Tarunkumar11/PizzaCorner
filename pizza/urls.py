from django.conf.urls import url
from .views import HomeView,Menushow

app_name = "pizza"

urlpatterns = [
    url('^$',HomeView,name='home'),
    url('^order/$',Menushow.as_view(),name='order'),
]