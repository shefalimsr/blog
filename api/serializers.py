from rest_framework import serializers
from .models import Blog,Login

class BlogSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=Blog 
		fields=('title','body')
			

class LoginSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=Login
		fields=('username','password')
			
		

