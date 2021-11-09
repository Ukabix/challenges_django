from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Work out for 1 hour everyday!",
    "february": "Read a book for 30 min everyday!",
    "march": "Learn Django for 30 mins everyday!",
    "april": "Pick up flowes twice a week!",
    "may": "Play bass for an hour every evening!",
    "june": "Clean your appartment every day!",
    "july": "Listen to new music every week!",
    "august": "Drink milk every morning!",
    "september": "Play chess once a week!",
    "october": "Sleep longer every weekend!",
    "november": "Cut on half coffee every morning!",
    "december": "Learn JS 1 hour everyday!"
}

# Create your views here.


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    # builds a path like /challenge/january
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported")
