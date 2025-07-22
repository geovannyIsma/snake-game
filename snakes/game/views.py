from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Score
import json

def game_view(request):
    """Main game page"""
    return render(request, 'game/snake.html')

@csrf_exempt
def save_score(request):
    """Save player score via AJAX"""
    if request.method == 'POST':
        data = json.loads(request.body)
        player_name = data.get('player_name', 'Anonymous')
        score = data.get('score', 0)
        
        Score.objects.create(
            player_name=player_name,
            score=score
        )
        
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def high_scores(request):
    """Display top 10 high scores"""
    scores = Score.objects.all()[:10]
    return render(request, 'game/high_scores.html', {'scores': scores})
