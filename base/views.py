from django.shortcuts import render,redirect,get_object_or_404
from base.models import patient
from base.forms import PatientModelForms
from django.db.models import Q #contains all the details regarding the serach query.

# Create your views here.
def home(request):
   return render(request,'home.html')
def search(request):
    search=request.GET.get('q') #
    if search:
      data=patient.objects.filter(
        Q(deleted=False),    #show records that are not deleted
        Q(name__icontains=search)|  #__icontains is used to search case-insensitive or remove case sensitivity.
        Q(age__icontains=search) |
        Q(gender__icontains=search) |
        Q(contact__icontains=search) |
        Q(consulting__icontains=search) 
        ) #__icontent__ is used to search case-insensitive or remove case sensitivity.
    else:
      data=patient.objects.filter(deleted=False) #filter is used to filter the data from the database.

    return render(request,'add_patient.html',{'data':data,'search':search})



def add_patient(request):                         #makes create patient form 
  form=PatientModelForms(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('read')
  return render(request,'add_patient.html',{'form':form})

def read(request):
    data = patient.objects.all()
    return render(request,'read.html',{'data':data})

def update(request,s_id):
    data = get_object_or_404(patient,id=s_id)
    form = PatientModelForms(request.POST or None, instance=data)
    if form.is_valid():
        form.save()
        return redirect('read')
    return render(request,'update.html',{'form':form})

def deleting(request,s_id):
    data = get_object_or_404(patient,id=s_id)
    if request.method=='POST':
        data.delete()
        return redirect('read')
    return render(request,'delete.html',{'data':data})