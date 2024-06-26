from django.shortcuts import render

# Create your views here:
def jinji(request):
    d={'name':'ammulbaby','age': 15}
    return render(request,'jinji_print.html',context=d)
