from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.Principal, name="Principal"),
	path('Login/', views.Login, name="Login"),
	path('Tienda/', views.Tienda, name="Tienda"),
	path('Carrito/', views.Carrito, name="Carrito"),
	path('Checkout/', views.Checkout, name="Checkout"),

]