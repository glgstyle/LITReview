
from django import views
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from review.models import Ticket, Review
from .forms.ticketForm import TicketForm
from .forms.reviewForm import ReviewForm
from django.contrib import messages
from django.shortcuts import get_object_or_404


@login_required
def flow(request):
    """View function for flow page of application."""
    tickets = Ticket.objects.all()
    return render(request, "flow.html", {'review': Review, 'ticket': Ticket, 'tickets': tickets})

def createTicket(request):
    """View function for createTicket page of application."""
    form = TicketForm(request.POST, request.FILES)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            existing_ticket = Ticket.objects.filter(title=ticket.title).exists()
            # check if this ticket already exists
            if existing_ticket:
                messages.error(request, 'Désolé un ticket a déjà été crée sur ce livre.', extra_tags='name')
            else:
                ticket.save()
                # redirect to a new URL:
                return HttpResponseRedirect('/flow/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = TicketForm()
    return render(request, 'create-ticket.html', {'form': form})

def confirmation(request):
    """View function for confirmation page of application."""
    return render(request, "confirmation.html")

def createReview(request):
    """View function for createReview page of application."""
    return render(request, "create-review.html")

def createReviewFromTicket(request, ticket_id):
    """View function for createReviewFromTicket page of application."""
    # ticket = get_object_or_404(Ticket, pk=ticket_id)
    ticket = Ticket.objects.get(pk=ticket_id)
    form = ReviewForm(request.POST)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        if form.is_valid():
            review = form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            # existing_review = Ticket.objects.filter(title=ticket.title).exists()
            # check if this ticket already exists
            # if existing_ticket:
            #     messages.error(request, 'Désolé un ticket a déjà été crée sur ce livre.', extra_tags='name')
            # else:
            review.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/flow/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ReviewForm()
    return render(request, "create-review-from-ticket.html", {'ticket': ticket, 'form': form})

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

# class  SampleView (views):
#      def  get_context_data ( self , ** kwargs ):
#          ticket = Ticket.objects.get(id=kwargs['user_id'])

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
    
