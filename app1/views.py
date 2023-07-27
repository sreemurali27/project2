from django.shortcuts import render
# Create your views here.
def data(request):
    D={'name':'sree','age':22}
    return render(request,'data.html',context= D)
