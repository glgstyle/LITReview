from django import views
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from review.forms.subscriptionForm import SubscriptionForm
from review.models import Ticket, Review
from .forms.ticketForm import TicketForm
from .forms.reviewForm import ReviewForm
from django.contrib import messages
from authentication.models import UserFollows
from django.db import IntegrityError
from itertools import chain
from django.db.models import CharField, Value

@login_required
def flow(request):
    reviews = get_users_viewable_reviews(request.user)
    # returns queryset of reviews
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

    tickets = get_users_viewable_tickets(request.user) 
    # returns queryset of tickets
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

    # combine and sort the two types of posts
    posts = sorted(chain(reviews, tickets), 
        key=lambda post: post.time_created, 
        reverse=True
    )
    tickets = Ticket.objects.all().order_by('time_created').reverse()
    return render(request, 'flow.html', context={'posts': posts})

def get_users_viewable_reviews(review_user):
    reviews = Review.objects.filter(user=review_user).order_by('time_created')
    return reviews

def get_users_viewable_tickets(ticket_user):
    tickets = Ticket.objects.filter(user=ticket_user).order_by('time_created')
    return tickets

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
            # existing_review = Review.objects.filter(ticket=ticket.pk).exists()
            # # check if this ticket already exists
            # if existing_review:
            #     messages.error(request, 'Désolé un ticket a déjà été crée sur ce livre.', extra_tags='name')
            # else:
            #     review.save()

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
    followed_users = get_followed_users(request)
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
                    messages.error(request, "cet utilisateur à été ajouté à votre liste.", extra_tags='name')
            except IntegrityError:
                messages.error(request, 'Vous ne pouvez pas suivre votre propre compte.', extra_tags='name')
        else:
            print('is not valid', form)
    else: # if a GET (or any other method) we'll create a blank form
        form = SubscriptionForm() 
    return render(request, "subscription.html",{'form': form, 'followed_users': followed_users})

def get_followed_users(request):
    followed_users = UserFollows.objects.filter(user=request.user)
    return followed_users

def unfollow(request, user_to_unfollow_id):
    followed_user = UserFollows.objects.get(pk=user_to_unfollow_id)
    if request.method == 'POST':
        followed_user.delete()
        return HttpResponseRedirect('/flow/confirmation/')
    return render(request, "delete.html", {'followed_user':followed_user})

def displayYourPosts(request):
    """View function for displayYourPosts page of application."""
    tickets = Ticket.objects.all().order_by('time_created').reverse()
    reviews = Review.objects.filter(user=request.user).order_by('time_created').reverse()  
    return render(request, "posts.html", {'tickets': tickets, 'reviews': reviews})

def modifyYourReview(request, review_id):
    """View function for modifyYourReview page of application."""
    review_to_modify = Review.objects.get(pk=review_id)
    form = ReviewForm(request.POST, instance=review_to_modify)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        if form.is_valid():
            review = form.save(commit=False)
            review.ticket = review_to_modify.ticket
            review.user = request.user
            review.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/flow/display_your_posts/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ReviewForm(instance=review_to_modify)
    return render(request, "modify-review.html", {'review':review_to_modify, 'form':form})

def deleteReview(request, review_id):
    review = Review.objects.get(pk=review_id)
    if request.method == 'POST':
        review.delete()
        return HttpResponseRedirect('/flow/confirmation/')
    return render(request, "delete.html", {'review':review})
        
def modifyYourTicket(request, ticket_id):
    """View function for modifyYourTicket page of application."""
    ticket_to_modify = Ticket.objects.get(pk=ticket_id)
    form = TicketForm(request.POST, request.FILES, instance=ticket_to_modify)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/flow/display_your_posts/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = TicketForm(instance=ticket_to_modify)
    return render(request, "modify-ticket.html", {'ticket':ticket_to_modify, 'form':form})

def deleteTicket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    if request.method == 'POST':
        ticket.delete()
        return HttpResponseRedirect('/flow/confirmation/')
    return render(request, "delete.html", {'ticket':ticket})

    
