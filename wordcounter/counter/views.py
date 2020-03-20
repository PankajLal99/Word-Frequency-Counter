from django.shortcuts import render,redirect
from . import scrap
from .forms import *
from .models import *
# Create your views here.
flag=False
message=str()
def index(request):
    form=UrlForm()
    if request.method=='POST':
        form=UrlForm(request.POST)
        if form.is_valid():
            url=form.cleaned_data.get('url')
            check=storage.objects.filter(url=url)
            for i in check:
                ch=i.key
            if not check:
                data=scrap.start(url)
                storage.objects.create(url=url,list_words=data)
                check=storage.objects.filter(url=url)
                for i in check:
                    ch=i.key
                return redirect('/results/'+str(ch))
            else:
                global flag
                flag=True
                return redirect('/results/'+str(ch))

    return render(request,'index.html',{'form':form})

def result(request,pk):
    global flag
    if  flag==False:
        message="This is a Freshly Scraped Data"
        
    elif flag==True:
        message="This is a Already Scraped Data"
        flag=False

    data=storage.objects.filter(key=pk)
    print(data)
    print(message)
    context={
        'msg':message
    }
    return render(request,'result.html')