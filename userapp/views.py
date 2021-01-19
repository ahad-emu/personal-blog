from userapp.models import Profile
from django.shortcuts import redirect, render
from django.views.generic import View, DetailView
from django.contrib.auth.models import User
from .forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import login_required

# Create your views here.

# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}')
#             return redirect('home')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'user/register.html', {'form': form})

class RegisterView(View):
    
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'user/register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')
        return render(request, 'user/register.html', {'form': form})

# @login_required
# def profileView(request):
#     u_form = UserUpdateForm(instance=request.user)
#     p_form = ProfileUpdateForm(instance=request.user.profile)
#     if request.method == 'POST':
#         u_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
#         p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, f'Your account has been updated')
#             return redirect('profile')
#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)
#     context = {
#         'u_form' : u_form,
#         'p_form' : p_form,
#     }
#     return render(request, 'user/profile.html', context)

class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance= request.user.profile)
        context = {
            'u_form' : u_form,
            'p_form' : p_form,
        }
        return render(request, 'user/profile.html', context)
    
    def post(self, request):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance= request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')

class ProfiletDetails(DetailView):
    model = Profile
    template_name = 'user/profiledetails.html'
    context_object_name = 'profile'