from django.urls import path

from home import views


app_name = 'home'


urlpatterns = [
	path('',views.show_post,name='show'),
	path('details/<int:id>/', views.show_detail_post, name='post_detail'),
]




