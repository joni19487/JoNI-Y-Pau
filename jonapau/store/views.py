from django.shortcuts import render

def Principal(request):
	context = {}
	return render(request, 'store/Principal.html', context)

def Login(request):
	context = {}
	return render(request, 'store/Login.html', context)

def Tienda(request):
	context = {}
	return render(request, 'store/Tienda.html', context)

def Carrito(request):
	context = {}
	return render(request, 'store/Carrito.html', context)

def Checkout(request):
	context = {}
	return render(request, 'store/Checkout.html', context)