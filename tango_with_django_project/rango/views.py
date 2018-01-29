from django.shortcuts import render
from django.http import HttpResponse

from rango.models import Category

# Create your views here.

def index(request):

	cat_dict= Category.objects.order_by('-likes')[:5]
	context_dic={'category':cat_dict}
	return render(request,'rango/index.html',context=context_dic)

	