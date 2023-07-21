from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import HttpResponse
from .models import Owner, Patient
from .forms import OwnerCreateForm, OwnerUpdateForm, PatientCreateForm, PatientUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# def login_view(request):
#   context = {
#     "login_view": "active"
#   }
#   if request.method == "POST":
#     username = request.POST["username"]
#     password = request.POST["password"]
#     # Add your code below:
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         # Use the returned user object in login()
#       login(request, user)
#       return redirect("home")
#     else:
#       return HttpResponse("invalid credentials")
#   return render(request, "registration/login.html", context)

@login_required
def home(request):
   context = {"name": "Django-er"}
   return render(request, "myapp/home.html", context)


class OwnerList(LoginRequiredMixin, ListView):
   model = Owner


class PatientList(LoginRequiredMixin, ListView):
   model = Patient


class OwnerCreate(LoginRequiredMixin, CreateView):
   model = Owner
   template_name = "myapp/owner_create_form.html"
   form_class = OwnerCreateForm


class PatientCreate(LoginRequiredMixin, CreateView):
   model = Patient
   template_name = "myapp/patient_create_form.html"
   form_class = PatientCreateForm


class OwnerUpdate(LoginRequiredMixin, UpdateView):
   model = Owner
   template_name = "myapp/owner_update_form.html"
   form_class = OwnerUpdateForm


class PatientUpdate(LoginRequiredMixin, UpdateView):
   model = Patient
   template_name = "myapp/patient_update_form.html"
   form_class = PatientUpdateForm


class OwnerDelete(LoginRequiredMixin, DeleteView):
   model = Owner
   template_name = "myapp/owner_delete_form.html"
   success_url = "/owner/list"


class PatientDelete(LoginRequiredMixin, DeleteView):
   model = Patient
   template_name = "myapp/patient_delete_form.html"
   success_url = "/patient/list"

# version 2
# from django.shortcuts import render
# from django.views.generic import ListView
# from django.views.generic.edit import CreateView, DeleteView, UpdateView
#
# from .models import Owner
# from .forms import OwnerCreateForm
#
# pets = [
#     {"petname": "Fido", "animal_type": "dog"},
#     {"petname": "Clementine", "animal_type": "cat"},
#     {"petname": "Cleo", "animal_type": "cat"},
#     {"petname": "Oreo", "animal_type": "dog"},
# ]
#
#
# def home(request):
#     context = {"name": "Djangoer", "pets": pets}
#     return render(request, "myapp/home.html", context)
#
#
# class OwnerList(ListView):
#     model = Owner
#
#
# def OwnerCreate(request):
#     # Add your code below:
#     if request.method == "POST":
#         newOwner = Owner()
#         newOwner.first_name = request.POST["first_name"]
#         newOwner.last_name = request.POST["last_name"]
#         newOwner.phone_number = request.POST["phone_number"]
#         newOwner.save()
#     return render(request, "myapp/owner_create_form.html")

# version 1
# from django.shortcuts import render
# from .models import Owner, Patient
# from django.views.generic import ListView
# from django.views.generic.edit import CreateView, DeleteView, UpdateView
# # Import Http404 below:
# from django.http import Http404
#
# def home(request):
#   # Add your code below:
#   try:
#     found_pet = Patient.objects.get(pk=2)
#   except Patient.DoesNotExist:
#     raise Http404()
#   context = {"name": "Djangoer", "pet": found_pet}
#   return render(request, "myapp/home.html", context)
#
# class OwnerList(ListView):
#   model = Owner
#   template_name = "myapp/owner_list.html"
#
# class PatientList(ListView):
#   model = Patient
#   template_name = "myapp/patient_list.html"
#
# class OwnerCreate(CreateView):
#   model = Owner
#   myapp = "myapp"
#   template_name = "%s/owner_create_form.html" % myapp
#   fields = ["first_name", "last_name", "phone"]
#
# class PatientCreate(CreateView):
#   model = Patient
#   template_name = "myapp/patient_create_form.html"
#   fields = ["animal_type", "breed", "pet_name", "age", "owner"]
#
# class OwnerUpdate(UpdateView):
#   model = Owner
#   template_name = "myapp/owner_update_form.html"
#   fields = ["first_name", "last_name", "phone"]
#
# class PatientUpdate(UpdateView):
#   model = Patient
#   template_name = "myapp/patient_update_form.html"
#   fields = ["animal_type", "breed", "pet_name", "age", "owner"]
#
# class OwnerDelete(DeleteView):
#   model = Owner
#   template_name = "myapp/owner_delete_form.html"
#
# class PatientDelete(DeleteView):
#   model = Patient
#   template_name = "myapp/patient_delete_form.html"
