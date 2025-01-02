
from django.contrib import admin
from .models import Category, Subscription, Series, Season, Episode, Plan

# Register your models here.

admin.site.register(Category)

class PlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'cost']
    class Meta:
        model = Plan
admin.site.register(Plan, PlanAdmin)

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['user', 'plan', 'start_date', 'end_date']
    readonly_fields = ['end_date']
    class Meta:
        model = Subscription
admin.site.register(Subscription, SubscriptionAdmin)

class SeriesAdmin(admin.ModelAdmin):
    list_display = ['title', 'release_date', 'premium_only']
    class Meta:
        model = Series
admin.site.register(Series, SeriesAdmin)

class SeasonAdmin(admin.ModelAdmin):
    list_display = ['series', 'season_number', 'type']
    readonly_fields = ['season_number']
    class Meta:
        model = Season
admin.site.register(Season, SeasonAdmin)

class EpisodeAdmin(admin.ModelAdmin):
    list_display = ['season', 'title', 'episode_number', 'release_date']
    readonly_fields = ['episode_number']
    class Meta:
        model = Episode
admin.site.register(Episode, EpisodeAdmin)