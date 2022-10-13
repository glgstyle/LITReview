from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .forms import *

def home(request):
    """View function for home page of application."""
    # return HttpResponse("<h1>Page d'accueil</h1>")
    return render(request, "index.html")

def registration(request):
    """View function for registration page of application."""
    return HttpResponse("<h1>Page d' inscription</h1>")

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