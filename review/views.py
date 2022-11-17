from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from review.models import Ticket, Review
from .forms.ticketForm import TicketForm
from .forms.reviewForm import ReviewForm
from .forms.ticketAndReviewForm import TicketAndReviewForm
from .forms.ticketAndReviewForm import ReviewFormset
from django.contrib import messages
from itertools import chain
from django.db.models import CharField, Value
from authentication.models import UserFollows


# ticket
def createTicket(request):
    """View function for createTicket page of application."""
    form = TicketForm(request.POST, request.FILES)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            existing_ticket = Ticket.\
                objects.filter(title=ticket.title).exists()
            # check if this ticket already exists
            if existing_ticket:
                messages.error(request, 'Désolé un ticket a déjà été crée '
                               'sur ce livre.', extra_tags='name')
            else:
                ticket.save()
                # redirect to a new URL:
                return HttpResponseRedirect('/flow/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = TicketForm()
    return render(request, 'create-ticket.html', {'form': form})


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
    return render(request, "modify-ticket.html", {'ticket': ticket_to_modify,
                  'form': form})


def deleteTicket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    if request.method == 'POST':
        ticket.delete()
        # return HttpResponseRedirect('/flow/confirmation/')
        return confirmation(request, return_url="flow/")
    return render(request, "delete.html", {'ticket': ticket})


# review
def createReview(request):
    """View function for createReview page of application."""
    if request.method == 'POST':
        print("on est dans requete post")
        ticket_and_review_form = TicketAndReviewForm(request.POST,
                                                     request.FILES)
        formset = ReviewForm(request.POST)
        if ticket_and_review_form.is_valid() and formset.is_valid():
            ticket_and_review_form = ticket_and_review_form.save(commit=False)
            ticket_and_review_form.user = request.user
            review = formset.save(commit=False)
            review.ticket = ticket_and_review_form
            review.user = request.user
            ticket_and_review_form = ticket_and_review_form.save()
            review.save()
            return HttpResponseRedirect('/flow/')
    else:
        ticket_and_review_form = TicketAndReviewForm()
        formset = ReviewFormset(queryset=Review.objects.none())
    return render(request, "create-review.html", {'ticket_and_review_form':
                  ticket_and_review_form, 'formset': formset})


def createReviewFromTicket(request, ticket_id):
    """View function for createReviewFromTicket page of application."""
    ticket = Ticket.objects.get(pk=ticket_id)
    form = ReviewForm(request.POST)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        if form.is_valid():
            review = form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/flow/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ReviewForm()
    return render(request, "create-review-from-ticket.html",
                  {'ticket': ticket, 'form': form})


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
    return render(request, "modify-review.html", {'review': review_to_modify,
                  'form': form})


def deleteReview(request, review_id):
    review = Review.objects.get(pk=review_id)
    if request.method == 'POST':
        review.delete()
        # return HttpResponseRedirect('/flow/confirmation/')
        return confirmation(request, return_url="flow/")
    return render(request, "delete.html", {'review': review})


# flow
@login_required
def flow(request):
    reviews = get_users_viewable_reviews(request.user)
    # returns queryset of reviews
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

    # query of followed_users_reviews
    followed_users = UserFollows.get_followed_users(request)
    followed_users_reviews = []
    for usr in followed_users:
        reviews_user = get_users_viewable_reviews(usr.followed_user).annotate(
            content_type=Value(
                'FOLLOWED_USER_REVIEWS_AND_REVIEWS_ON_MY_TICKETS',
                CharField()))
        followed_users_reviews = chain(followed_users_reviews, reviews_user)

    # reviews on my ticket but exclude reviews on my ticket because already
    # in reviews variable
    reviews_on_my_tickets = Review.objects.filter(
        ticket__user=request.user).exclude(user=request.user).order_by(
            'time_created').annotate(content_type=Value(
                'FOLLOWED_USER_REVIEWS_AND_REVIEWS_ON_MY_TICKETS',
                CharField()))

    tickets = Ticket.objects.all()
    # returns queryset of tickets
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

    # combine and sort the two types of posts
    try:
        posts = sorted(
            chain(reviews, tickets, followed_users_reviews,
                  reviews_on_my_tickets),
            key=lambda post: post.time_created, reverse=True)
    except UnboundLocalError:
        posts = sorted(chain(reviews, tickets),
                       key=lambda post: post.time_created,
                       reverse=True)
    return render(request, 'flow.html', context={'posts': posts})


def get_users_viewable_reviews(review_user):
    reviews = Review.objects.filter(user=review_user).order_by('time_created')
    return reviews


def get_users_viewable_tickets(ticket_user):
    tickets = Ticket.objects.filter(user=ticket_user).order_by('time_created')
    return tickets


# posts
def displayYourPosts(request):
    """View function for displayYourPosts page of application."""
    tickets = Ticket.objects.all().order_by('time_created').reverse()
    reviews = Review.objects.filter(user=request.user).\
        order_by('time_created').reverse()
    my_tickets = Ticket.objects.filter(user=request.user).\
        order_by('time_created').reverse()
    return render(request, "posts.html", {'tickets': tickets,
                  'reviews': reviews, 'my_tickets': my_tickets})


#  success page
def confirmation(request, return_url):
    """View function for confirmation page of application."""
    return render(request, "confirmation.html", {'return_url': return_url})
