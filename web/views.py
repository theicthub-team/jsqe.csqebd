from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'web/home.html')


def editors_profile(request):
    return render(request, 'web/profile.html')


def board_member(request):
    return render(request, 'web/board_member.html')


def manuscript(request):
    return render(request, 'web/manuscript.html')


def contact(request):
    return render(request, 'web/contact.html')