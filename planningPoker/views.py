from django.shortcuts import render


def home(request):
    print(request.session.session_key)
    return render(request, 'home.html')
