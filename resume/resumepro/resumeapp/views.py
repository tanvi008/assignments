from multiprocessing.sharedctypes import Value

from django.shortcuts import render
from .models import UserInfo,  pdf
from .forms import PdfForm, UserForm
# from resumepro.resumeapp import forms

#login/register--> want to upload resume or want us to make it for you ?
# upload--> pdf model--> convert pdf to text when submit is clicked--> store in dictionary as key Value
# auto generated--> directly store text in database in form of dictionary


def home(request):
    return render(request, 'index.html')


def users(request):
    form = UserForm()
    if request.method == "POST":
        form = form(request.POST)
        if form.is_valid():
            form.save()

    context={"form": form}
    return render(request, 'upload.html', context)
 
    

def pdfview(request):
    form = PdfForm()
    if request.method == "POST":
        print(request.FILES)
        form = form(request.FILES)
        
        if form.is_valid():
            data = pdf.objects.create(document=request.FILES)
            data.save()

 # pdfs =pdf.objects.all()
    # context = {'docs':pdfs, 'form':form}
    return render(request, 'pdf.html', {"form":form})






