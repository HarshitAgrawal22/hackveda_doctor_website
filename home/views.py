from django.shortcuts import render
from .models import Appointment
# Create your views here.

def home(request):
    if request.method == "POST":
        print("load")
        appoint=Appointment.objects.create(name=request.POST.get("name"),phone_number=
        request.POST.get("phone_number"),email=request.POST.get("email"),date=request.POST.get("date"),message=request.POST.get("message"))
        appoint.save()
        
        
        
        return render(request,"index.html")
    return render(request,"index.html")