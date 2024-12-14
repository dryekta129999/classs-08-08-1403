from django.urls import path,include

from home import views


app_name = 'home'


urlpatterns = [
	path('',views.show_post,name='home'),
	path('detail/<int:id>/',views.show_post_detail,name='detail' ),
]




