from django.shortcuts import render, get_object_or_404

def Index(request):

    return render(request, 'home/index.html')