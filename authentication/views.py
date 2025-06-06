from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#auth_user acts as model for authentication
# Create your views here.
def signup(request):
    if request.method =='POST':
        User.objects.create_user(
            first_name=request.POST['firstname'],
            last_name=request.POST['lastname'],
            username=request.POST['username'],  
            email=request.POST['email'],
            password=request.POST['password'],
        )
        return redirect('signin')
    return render(request,'signup.html')

def signin(request):
    if request.method == 'POST':
        user = authenticate(request,
            username=request.POST['username'],
            password=request.POST['password'],
        )
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            

    return render(request,'signin.html')


@login_required(login_url='signin')
def profile(request):
    return render(request,'profile.html',{'user': request.user})

@login_required(login_url='signin')
def update_profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.email = request.POST['email']
        user.username = request.POST['username']
        user.save()
        messages.success(request, 'Profile updated successfully')
        return redirect('profile')
    return render(request, 'update_profile.html', {'user': request.user})

@login_required(login_url='signin')
def update_password(request):
    if request.method == 'POST':
        user = request.user
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        if not user.check_password(old_password):
            messages.error(request, 'Old password is incorrect')
            

        elif new_password != confirm_password:
            messages.error(request, 'New passwords do not match')
            
        else:
            user.set_password(new_password) #set_password is used encrypt the password for security
            user.save()
            update_session_auth_hash(request, user) #update_session_auth_hash is used to update the session with the new password
            messages.success(request, 'Password updated successfully')
            return redirect('signin')

    return render(request,'update_password.html')

@login_required(login_url='signin')
def signout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('signin')