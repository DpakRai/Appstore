from django.shortcuts import render
from . forms import blockForm
from . models import block

def index(request):
    if request.method =="GET":

        form =  blockForm()

    else:
        form = blockForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return render(request, 'block/index.html')


            except:
                message = "data not saved try again"   
                return render(request, 'block/index.html',{'message': message})
 
    return render(request, 'block/index.html',{'form': form})
