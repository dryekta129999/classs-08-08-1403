from django.urls import path

from . import views


app_name = 'home'


urlpatterns = [
	path('',views.show_post,name='show'),
]