from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Owner, Patient, Appointment
from .forms import OwnerCreateForm, OwnerUpdateForm, PatientCreateForm, PatientUpdateForm, AppointmentCreateForm, \
    AppointmentUpdateForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


# Complete your SignUp view below:
class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


@login_required
def home(request):
    context = {"name": request.user}
    return render(request, "myapp/home.html", context)


class OwnerList(LoginRequiredMixin, ListView):
    model = Owner


class PatientList(LoginRequiredMixin, ListView):
    model = Patient


class AppointmentList(LoginRequiredMixin, ListView):
    model = Appointment


class OwnerCreate(LoginRequiredMixin, CreateView):
    model = Owner
    template_name = "myapp/owner_create_form.html"
    form_class = OwnerCreateForm


class PatientCreate(LoginRequiredMixin, CreateView):
    model = Patient
    template_name = "myapp/patient_create_form.html"
    form_class = PatientCreateForm


class AppointmentCreate(LoginRequiredMixin, CreateView):
    model = Appointment
    template_name = "myapp/appointment_create_form.html"
    form_class = AppointmentCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class OwnerUpdate(LoginRequiredMixin, UpdateView):
    model = Owner
    template_name = "myapp/owner_update_form.html"
    form_class = OwnerUpdateForm


class PatientUpdate(LoginRequiredMixin, UpdateView):
    model = Patient
    template_name = "myapp/patient_update_form.html"
    form_class = PatientUpdateForm


class AppointmentUpdate(LoginRequiredMixin, UpdateView):
    model = Appointment
    template_name = "myapp/appointment_update_form.html"
    form_class = AppointmentUpdateForm


class OwnerDelete(LoginRequiredMixin, DeleteView):
    model = Owner
    template_name = "myapp/owner_delete_form.html"
    success_url = "/owner/list"


class PatientDelete(LoginRequiredMixin, DeleteView):
    model = Patient
    template_name = "myapp/patient_delete_form.html"
    success_url = "/patient/list"


class AppointmentDelete(LoginRequiredMixin, DeleteView):
    model = Appointment
    template_name = "myapp/appointment_delete_form.html"
    success_url = "/appointment/list"
