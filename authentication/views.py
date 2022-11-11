from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .forms.registrationForm import NewUserForm
from .forms.subscriptionForm import SubscriptionForm
from .forms.loginForm import loginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import UserFollows
from review.views import *
from django.db import IntegrityError


# registration
def registration(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewUserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            email = form.cleaned_data.get('your_email')
            password = form.cleaned_data.get('your_password')
            user = User()
            user.username=email
            usernames = User.objects.filter(is_active=True).values_list('username', flat=True)
            if email in usernames:
                messages.error(request, 'Désolé ce mail existe déjà.', extra_tags='name')
            else:
                # encrypt password
                user.set_password(password)
                user.save()
                # redirect to a new URL:
                return HttpResponseRedirect('/registration-confirmation/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewUserForm()
    return render(request, 'registration.html', {'form': form})

def RegistrationConfirmation(request):
    """View function for registration confirmation page of application."""
    return render(request, "registration-confirmation.html")

# login/logout
def login_page(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/flow/')
    form = loginForm()
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password'),
            )
            if user is not None:
                login(request, user)
                # return HttpResponseRedirect('/flow/')
                return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

            else:
                messages.error = 'Login failed!'
    return render(
        request, 'index.html', context={'form': form})

def logout_user(request):
    logout(request)
    # Redirect back to index page.
    return redirect('/')

# subscription
def subscription(request):
    """View function for subscription page of application."""
    followed_users = UserFollows.get_followed_users(request)
    followers = UserFollows.get_followed_by(request)
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            user_to_follow = form.cleaned_data.get('followed_user')
            userFollow = UserFollows()
            userFollow.user = request.user
            existing_user = User.objects.filter(username=user_to_follow, is_active=True).exists()
            if existing_user:
                get_user_to_follow = User.objects.get(username=user_to_follow)  
            get_request_user = User.objects.get(username=request.user)
            # search in database if user_to_follow already followed by this user
            user_followed = UserFollows.objects.filter(user=request.user, followed_user__username=user_to_follow).exists()
            try:
                # if user to follow exists record it
                if not existing_user:
                    messages.error(request, "Cet utilisateur n'existe pas, veuillez recommencer.", extra_tags='name')
                    # if user try to follow himself
                elif get_user_to_follow.username == get_request_user.username :
                    messages.error(request, 'Vous ne pouvez pas suivre votre propre compte.', extra_tags='name')
                # if we already follow him
                elif user_followed:
                    messages.error(request, 'Vous suivez déjà cet utilisateur.', extra_tags='name')
                else:
                    userFollow.followed_user = get_user_to_follow
                    userFollow.save()
                    messages.success(request, "Cet utilisateur à été ajouté à votre liste.", extra_tags='name')
            except IntegrityError:
                messages.error(request, 'Vous ne pouvez pas suivre votre propre compte.', extra_tags='name')
            except TypeError:
                messages.error(request, 'Vous suivez déjà cet utilisateur.', extra_tags='name')
        else:
            print('is not valid', form)
    else: # if a GET (or any other method) we'll create a blank form
        form = SubscriptionForm() 
    return render(request, "subscription.html",{'form': form, 'followed_users': followed_users, 'followers': followers})

def unfollow(request, user_to_unfollow_id):
    followed_user = UserFollows.objects.get(pk=user_to_unfollow_id)
    if request.method == 'POST':
        followed_user.delete()
        # return HttpResponseRedirect('/flow/confirmation/')
        return confirmation(request, return_url="flow/subscription/")
    return render(request, "delete.html", {'followed_user':followed_user})
