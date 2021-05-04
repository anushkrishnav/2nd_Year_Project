from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView

from .models import CustomUser, Profile

from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, ProfileUpdate
from .models import CustomUser
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect

from django.contrib import messages 
# Create your views here.

def signupView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            signup_user = CustomUser.objects.get(username=username)
            employer_group = Group.objects.get(name='Employer')
            employer_group.user_set.add(signup_user)

            Profile.objects.create(
                user=user
            )
            
            messages.success(request, ('Your Form Has Been Submitted Successfully'))
            return redirect('signin')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form':form})
    
def employerSignupView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.instance.is_employer = True
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = CustomUser.objects.get(username=username)
            employer_group = Group.objects.get(name='Employer')
            employer_group.user_set.add(signup_user)
            return redirect('signin')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form':form})

def signinView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('signin')
            else:
                return redirect('signup')
    else:
        form = AuthenticationForm()
    return render(request,'signin.html', {'form':form})

def signoutView(request):
    logout(request)
    return redirect('signin')

def ProfileView(request):

    context = {
        'Profile': Profile,
    }

    return render(request, 'accounts/profile_detail.html', context=context)

class UpdateProfileView(UpdateView):

    model = Profile
    template_name = 'accounts/profile_update.html'
    fields = ['image', 'description', 'cv']
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        pass


def profileUpdate(request):
    print(request)
    if request.method == "POST":
        form = ProfileUpdate(request.POST, request.FILES, instance=request.user.profile)
       
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/profile/')
        
        
    else:
        form = ProfileUpdate()

    return render(request, 'accounts/profile_update.html', {'form': form})