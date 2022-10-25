from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from review.models import Ticket, Review
from .forms.ticketForm import ticketForm
from django.contrib import messages
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User


@login_required
def flow(request):
    """View function for flow page of application."""
    return render(request, "flow.html", {'review': Review, 'ticket': Ticket})

def createTicket(request):
    """View function for createTicket page of application."""
    form = ticketForm(request.POST, request.FILES)
    if form.is_valid():
        ticket = form.save(commit=False)
        ticket.user = request.user
        ticket.save()
        return redirect('/flow/')
    # # if this is a POST request we need to process the form data
    # if request.method == 'POST':
    #     # create a form instance and populate it with data from the request:
    #     form = ticketForm(request.POST)
    #     # check whether it's valid:
    #     if form.is_valid():
    #         title = form.cleaned_data.get('title')
    #         description = form.cleaned_data.get('description')
    #         image = form.get('image')
    #         user = User.objects.get(pk=request.user)
    #         time_created = datetime.datetime.now
    #         ticket = Ticket()
    #         ticket.title = title
    #         ticket.description = description
    #         ticket.image = image
    #         ticket.user = user
    #         ticket.time_created = time_created
    #         tickets = ticket.objects.filter(is_active=True).values_list('ticket', flat=True)
    #         if ticket in tickets:
    #             messages.error(request, 'Désolé un ticket a déjà été crée sur ce livre.', extra_tags='name')
    #         else:
    #             ticket.save()
    #             # redirect to a new URL:
    #             return HttpResponseRedirect('')
    # # if a GET (or any other method) we'll create a blank form
    # else:
    #     form = ticketForm()


    return render(request, 'create-ticket.html', {'form': form})
    # return render(request, "create-ticket.html")

def confirmation(request):
    """View function for confirmation page of application."""
    return render(request, "confirmation.html")

def createReview(request):
    """View function for createReview page of application."""
    return render(request, "create-review.html")

def createReviewFromTicket(request):
    """View function for createReviewFromTicket page of application."""
    return render(request, "create-review-from-ticket.html")
    
def subscription(request):
    """View function for subscription page of application."""
    return render(request, "subscription.html")

def displayYourPosts(request):
    """View function for displayYourPosts page of application."""
    return render(request, "posts.html")

def modifyYourReview(request):
    """View function for modifyYourReview page of application."""
    return render(request, "modify-review.html")

def modifyYourTicket(request):
    """View function for modifyYourTicket page of application."""
    return render(request, "modify-ticket.html")


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

# Post a review

# def postReview():
#     review = Review()

# Post a ticket

# def postTicket():
#     ticket = Ticket()
    
