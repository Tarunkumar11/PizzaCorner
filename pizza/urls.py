from django.conf.urls import url
from .views import HomeView

app_name = "pizza"

urlpatterns = [
    url('^$',HomeView,name='home')
]