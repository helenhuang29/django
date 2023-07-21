from django.shortcuts import render
from .models import Owner, Patient
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
# Import Http404 below:
from django.http import Http404

def home(request):
  # Add your code below:
  try:
    found_pet = Patient.objects.get(pk=2)
  except Patient.DoesNotExist:
    raise Http404()
  context = {"name": "Djangoer", "pet": found_pet}
  return render(request, "myapp/home.html", context)

class OwnerList(ListView):
  model = Owner
  template_name = "myapp/owner_list.html"

class PatientList(ListView):
  model = Patient
  template_name = "myapp/patient_list.html"

class OwnerCreate(CreateView):
  model = Owner
  vetoffice = "myapp"
  template_name = "%s/owner_create_form.html" % vetoffice
  fields = ["first_name", "last_name", "phone"]

class PatientCreate(CreateView):
  model = Patient
  template_name = "myapp/patient_create_form.html"
  fields = ["animal_type", "breed", "pet_name", "age", "owner"]

class OwnerUpdate(UpdateView):
  model = Owner
  template_name = "myapp/owner_update_form.html"
  fields = ["first_name", "last_name", "phone"]

class PatientUpdate(UpdateView):
  model = Patient
  template_name = "myapp/patient_update_form.html"
  fields = ["animal_type", "breed", "pet_name", "age", "owner"]

class OwnerDelete(DeleteView):
  model = Owner
  template_name = "myapp/owner_delete_form.html"

class PatientDelete(DeleteView):
  model = Patient
  template_name = "myapp/patient_delete_form.html"