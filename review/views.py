from django.contrib.auth.decorators import login_required
from .forms import TicketForm, ReviewForm, UserFollowsForm
from django.shortcuts import redirect, render
from .models import Ticket, Review, UserFollows
from . import models
from itertools import chain
from django.db.models import Q

from django.core.paginator import Paginator


@login_required
def ticket_create(request):
    form = TicketForm()
    print("La méthode de requête est : ", request.method)
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            # définit le lecteur à l’utilisateur courant avant d’enregistrer le modèle
            ticket.user = request.user
            ticket.save()
            print("okkk", form.cleaned_data)
            print("Les données POST sont : ", request.POST)
            return redirect("my_posts")
    else:
        form = TicketForm()
    return render(request, "review/ticket_create.html", {"form": form})


@login_required
def ticket_update(request, id):
    ticket = Ticket.objects.get(id=id)
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect("my_posts")
    else:
        form = TicketForm(instance=ticket)
    return render(request, "review/ticket_update.html", {"form": form})


@login_required
def ticket_delete(request, id):
    ticket = Ticket.objects.get(id=id)
    if request.method == "POST":
        ticket.delete()
        return redirect("my_posts")
    return render(request, "review/ticket_delete.html", {"ticket": ticket})


@login_required
def review_create(request, id):
    ticket = Ticket.objects.get(id=id)
    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            # définit le lecteur à l’utilisateur courant avant d’enregistrer le modèle
            review.user = request.user
            review.ticket = ticket
            ticket.review = True
            ticket.save()
            review.save()
            return redirect("feed")
    else:
        form = ReviewForm()
    return render(
        request, "review/review_create.html", {"form": form, "ticket": ticket}
    )


@login_required
def review_update(request, id):
    review = Review.objects.get(id=id)
    ticket = review.ticket
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect("my_posts")
    else:
        form = ReviewForm(instance=review)
    return render(
        request, "review/review_update.html", {"form": form, "ticket": ticket}
    )


@login_required
def review_delete(request, id):
    review = Review.objects.get(id=id)
    ticket = review.ticket
    print("review.ticket: ", review.ticket)
    print("ticket.review: ", ticket.review)
    if request.method == "POST":
        ticket.review = False
        ticket.save()
        print("ticket.review après save: ", ticket.review)
        review.delete()
        return redirect("my_posts")
    return render(request, "review/review_delete.html", {"review": review})


@login_required
def ticket_and_review_create(request):
    ticket_form = TicketForm()
    review_form = ReviewForm()
    if request.method == "POST":
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)
        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.review = True
            ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect("my_posts")
    context = {
        "ticket_form": ticket_form,
        "review_form": review_form,
    }
    return render(request, "review/ticket_and_review_create.html", context=context)


@login_required
def my_posts(request):
    tickets = Ticket.objects.filter(user__id=request.user.id)
    reviews = Review.objects.filter(user__id=request.user.id)
    return render(
        request,
        "review/my_posts.html",
        context={"tickets": tickets, "reviews": reviews},
    )


@login_required
def user_follows(request):
    form = UserFollowsForm(instance=request.user)
    followed_users = models.UserFollows.objects.filter(user__id=request.user.id)
    subscribed_users = models.UserFollows.objects.filter(
        followed_user__id=request.user.id
    )
    print("followed_users : ", followed_users)
    if request.method == "POST":
        form = UserFollowsForm(request.POST)
        if form.is_valid():
            user_follows = form.save(commit=False)
            user_follows.user = request.user
            user_follows.save()
            form.save()
            return redirect("user_follows")
        else:
            form = UserFollowsForm()
    return render(
        request,
        "review/user_follows_form.html",
        {
            "followed_users": followed_users,
            "subscribed_users": subscribed_users,
            "form": form,
        },
    )


@login_required
def user_follows_unsubscribe(request, id):
    followed_user = UserFollows.objects.get(id=id)
    if request.method == "POST":
        followed_user.delete()
        return redirect("user_follows")
    return render(
        request,
        "review/user_follows_unsubscribe.html",
        {"user_followed": followed_user},
    )


@login_required
def feed(request):
    reviews = get_users_viewable_reviews(request)
    viewable_tickets = get_users_viewable_tickets(request)
    posts = sorted(
        chain(reviews, viewable_tickets),
        key=lambda post: post.time_created,
        reverse=True,
    )
    paginator = Paginator(posts, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}
    return render(request, "review/feed.html", context=context)


@login_required
def get_users_viewable_reviews(request):
    list_viewable_reviews = []
    my_tickets = Ticket.objects.filter(user__id=request.user.id)
    reviews_for_my_tickets = Review.objects.filter(ticket__in=my_tickets)
    my_reviews = Review.objects.filter(
        Q(user__id=request.user.id) & ~Q(ticket__in=my_tickets)
    )
    list_viewable_reviews.extend(my_reviews)
    list_viewable_reviews.extend(reviews_for_my_tickets)
    users_followed = UserFollows.objects.filter(user__id=request.user.id)
    for user in users_followed:
        reviews = Review.objects.filter(
            Q(user__id=user.followed_user.id) & ~Q(ticket__in=my_tickets)
        )
        list_viewable_reviews.extend(reviews)
    return list_viewable_reviews


@login_required
def get_users_viewable_tickets(request):
    users_followed = UserFollows.objects.filter(user__id=request.user.id)
    list_viewable_tickets = []
    my_tickets = Ticket.objects.filter(user__id=request.user.id)
    list_viewable_tickets.extend(my_tickets)
    for user in users_followed:
        tickets = Ticket.objects.filter(user__id=user.followed_user.id)
        list_viewable_tickets.extend(tickets)
    return list_viewable_tickets
