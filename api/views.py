from django.shortcuts import render
from rest_framework import viewsets
from .models import Blog,Login
from .serializers import BlogSerializer,LoginSerializer
# Create your views here.

# def home(request):
# 	return render(request,'index.html')

class BlogViewSet(viewsets.ModelViewSet):
	queryset=Blog.objects.all()
	serializer_class=BlogSerializer

class LoginViewSet(viewsets.ModelViewSet):
	queryset=Login.objects.all()
	serializer_class=LoginSerializer
		
