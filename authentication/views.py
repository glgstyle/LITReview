from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .forms.registrationForm import NewUserForm
from .forms.loginForm import loginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def RegistrationConfirmation(request):
    """View function for registration confirmation page of application."""
    return render(request, "registration-confirmation.html")

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
    
def login_page(request):
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
    return redirect('accueil')

# # Image_book

# def book_image_view(request):
  
#     if request.method == 'POST':
#         form = makeATicketForm(request.POST, request.FILES)
  
#         if form.is_valid():
#             form.save()
#             return redirect('success')
#     else:
#         form = makeATicketForm()
#     return render(request, 'hotel_image_form.html', {'form' : form})
  
  
# def success(request):
#     return HttpResponse('successfully uploaded')