from django.shortcuts import render

# Create your views here.

def jinja_print1(request):
    d={'name':'venkat','mobile':'8787489341'}
    return render(request,'jinja_print1.html',context=d)