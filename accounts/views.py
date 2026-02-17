from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomAuthenticationForm, PasswordResetEmailForm
from django.contrib.auth import authenticate, login, logout
import random
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.forms import SetPasswordForm
from .models import Freelancer
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'signup.html', context)

def signin(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = CustomAuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'signin.html', context)


def signout(request):
    logout(request)
    return redirect('signin')

def genrate_otp():
    otp = str(random.randint(100000, 999999))
    return otp

def forgot_password(request):
    if request.method == "POST":
        form = PasswordResetEmailForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = CustomUser.objects.get(email=email)
                otp = genrate_otp()

                request.session['otp'] = otp
                request.session['request_user'] = user.id

                send_mail(
                        "Password reset OTP",
                        f"Your OTP for password reset is : {otp}",
                        settings.EMAIL_HOST_USER,
                        [user.email],
                        fail_silently=False,
                )
                return redirect('verify_otp')


            except CustomUser.DoesNotExist:
                messages.error(request,"email does not exist")

    else:
        form = PasswordResetEmailForm()
    context = {
        'form': form
    }
    return render(request, 'forgot_password.html', context)

def verifyOtp(request):
    if request.method == "POST":
        entered_otp = request.POST['otp']
        otp_stored = request.session.get('otp')

        if entered_otp == otp_stored:
            user_id = request.session['request_user']

            if user_id:
                user = CustomUser.objects.get(id=user_id)
                return redirect('reset_password',user_id= user.id)
            else:
                print("session expired========")

        else:
            messages.error(request,"invalid otp")


    return render(request,'verify_otp.html')




def resetPassword(request,user_id):
    user= CustomUser.objects.get(id = user_id)
    if request.method == "POST":
        form= SetPasswordForm(user=user,data=request.POST)
        if form.is_valid():
            form.save()

            if 'otp' in request.session:
                del request.session['otp']
            if 'request_user' in request.session:
                del request.session['request_user']

            return redirect("signin") 
    else:
        form= SetPasswordForm(user=user)

        context={
            'form': form
        }
    return render(request,"reset_password.html",context)


def search_freelancers(request):
    freelancers_list = Freelancer.objects.all()
    return render(request, 'search_freelancers.html', {'freelancers_list': freelancers_list})


@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('freelancers_profile', user_id=user.id)
    else:
        form = CustomUserCreationForm(instance=user)
    return render(request, 'edit_profile.html', {'form': form})

@login_required
def delete_profile(request):
    user = request.user
    if request.method == 'POST':
        user.delete()
        return redirect('index')
    return render(request, 'delete_profile.html')