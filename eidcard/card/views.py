from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import EidCard

def home(request):
    return render(request, 'home.html')

def generate_card(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        image = request.FILES.get('image')

        if not (name and message and image):
            return JsonResponse({'error': 'All fields are required.'})

        card = EidCard.objects.create(name=name, message=message, image=image)
        link = request.build_absolute_uri(f"/card/{card.id}/")
        return JsonResponse({'link': link})

def card_detail(request, card_id):
    card = get_object_or_404(EidCard, id=card_id)
    return render(request, 'card_detail.html', {'card': card})
