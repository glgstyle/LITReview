from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .registrationForm import NewUserForm
from django.contrib.auth import authenticate
from django.contrib import messages

def home(request):
    """View function for home page of application."""
    return render(request, "index.html")

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
                # return redirect('/registration/')
            else:
                # encrypt password
                user.set_password(password)
                user.save()
                # redirect to a new URL:
                return HttpResponseRedirect('/registration-confirmation/')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            # return redirect('home')
            # process the data in form.cleaned_data as required
            # ...

            # renvoyer vers un lien pour se connecter

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewUserForm()

    return render(request, 'registration.html', {'form': form})
    
def login():
    user = authenticate(username='john', password='secret')
    if user is not None:
        # A backend authenticated the credentials
        pass
    else:
        pass
        # No backend authenticated the credentials


# fonction login 
# si l'utilisateur existe et que sont mot de passe est correct log le sur flow/

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