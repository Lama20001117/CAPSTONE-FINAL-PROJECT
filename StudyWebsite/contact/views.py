from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import ContactSupport

# Create your views here.
def contact_view(request:HttpRequest):
    if request.method == 'POST':
        
        try:
            new_con = ContactSupport(
                user=request.POST["user"],  
                email=request.POST["email"], 
                message= request.POST["message"]
            )
            
            new_con.save()
            return redirect("contact:message_view")
        except Exception as e:
                    print(e)
        

    return render(request, "contact/contact.html")
def message_view(request:HttpRequest):
    if not request.user.is_superuser:
        return render(request, "main/not_found.html")
    contacts = ContactSupport.objects.all()
    return render(request, "contact/message.html", {"contacts" : contacts })