from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .forms import *

# def home(request):
#     """View function for home page of application."""
#     return HttpResponse("<h1>Page d'accueil</h1>")

def flow(request):
    """View function for flow page of application."""
    return HttpResponse("<h1>Page de flux</h1>")

def createTicket(request):
    """View function for createTicket page of application."""
    return HttpResponse("<h1>Page création d'un ticket</h1>")

def createReview(request):
    """View function for createReview page of application."""
    return HttpResponse("<h1>Page créer une critique (pas en rapport avec un ticket)</h1>")

def createReviewFromTicket(request):
    """View function for createReviewFromTicket page of application."""
    return HttpResponse("<h1>Page créer une critique (en reponse à un ticket)</h1>")

def displayYourPosts(request):
    """View function for displayYourPosts page of application."""
    return HttpResponse("<h1>Page voir vos posts</h1>")

def modifyYourReview(request):
    """View function for modifyYourReview page of application."""
    return HttpResponse("<h1>Page modifier votre critique</h1>")

def modifyYourTicket(request):
    """View function for modifyYourTicket page of application."""
    return HttpResponse("<h1>Page modifier votre ticket</h1>")

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