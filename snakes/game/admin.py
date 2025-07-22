from django.contrib import admin
from .models import Score

@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('player_name', 'score', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('player_name',)
    readonly_fields = ('created_at',)
