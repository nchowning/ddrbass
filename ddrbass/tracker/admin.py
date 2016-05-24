from django.contrib import admin

from .models import (
    Difficulty,
    Style,
    Grade,
    Song,
    Chart,
    Mix,
    Score,
)


class GenericNameAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class GenericNameCodeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'code',
    )


class SongAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'name_translation',
        'artist',
        'artist_translation',
        'bpm',
        'bpm_max',
        'genre',
    )

    search_fields = (
        'name',
        'name_translation',
        'artist'
        'artist_translation',
        'genre',
    )

    list_filter = (
        'genre',
    )


class ChartAdmin(admin.ModelAdmin):
    list_display = (
        'song',
        'style',
        'difficulty',
        'difficulty_rating',
        'difficulty_rating_old',
    )

    list_filter = (
        'style',
        'difficulty',
        'difficulty_rating',
        'difficulty_rating_old',
    )


class MixAdmin(admin.ModelAdmin):
    list_filter = (
        'name',
        'release',
        'region',
    )


class ScoreAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General', {'fields': [
            'user',
            'chart',
            'mix',
        ]}),
        ('Score', {'fields': [
            'passing',
            'marvelous',
            'perfect',
            'great',
            'good',
            'boo',
            'miss',
            'ok',
        ]}),
        ('Social', {'fields': [
            'comment',
            'picture_url',
            'video_url',
        ]}),
    ]

    list_display = (
        'user',
        'chart',
        'machine_score',
        'passing',
    )

    list_filter = (
        'user',
    )


admin.site.register(Difficulty, GenericNameCodeAdmin)
admin.site.register(Style, GenericNameCodeAdmin)
admin.site.register(Grade, GenericNameAdmin)

admin.site.register(Song, SongAdmin)
admin.site.register(Chart, ChartAdmin)
admin.site.register(Mix, MixAdmin)

admin.site.register(Score, ScoreAdmin)
