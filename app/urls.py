from django.urls import path
from .views import home_view,register_page,login_page,logout_page,update_page,delete_view

urlpatterns = [

	path("",home_view,name="home"),
	path("register/",register_page,name="register"),
	path("login/",login_page,name="login"),
	path("logout/",logout_page,name="logout"),
	path("update/<str:id>",update_page,name="update"),
	path("delete/<str:id>",delete_view,name="delete"),

	
]