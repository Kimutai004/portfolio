from django.shortcuts import render

def index(request):
    return render(request, 'portfolio/index.html')  # Correct template path