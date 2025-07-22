from django.db import models
from django.utils import timezone

class Score(models.Model):
    player_name = models.CharField(max_length=50)
    score = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-score', '-created_at']
    
    def __str__(self):
        return f"{self.player_name}: {self.score}"
