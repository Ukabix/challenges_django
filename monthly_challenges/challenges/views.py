from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def january(request):
    return HttpResponse("Work out for 1 hour everyday!")


def february(request):
    return HttpResponse("Read a book for 30 min everyday!")


def march(request):
    return HttpResponse("Learn Django for 30 mins everyday!")


def monthly_challenge_by_number(request, month):
    return HttpResponse(month)


def monthly_challenge(request, month):
    challenge_text = ""
    if month == "january":
        challenge_text = "Work out for 1 hour everyday!"
    elif month == "february":
        challenge_text = "Read a book for 30 min everyday!"
    elif month == "march":
        challenge_text = "Learn Django for 30 mins everyday!"
    else:
        return HttpResponseNotFound("This month is not supported")
    return HttpResponse(challenge_text)
