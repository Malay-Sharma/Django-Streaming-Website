
from django.contrib import admin
from .models import Category, Subscription, Series, Episode, Plan

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
    list_display = ['title', 'type', 'season_number', 'premium_only']
    readonly_fields = ['season_number']
    class Meta:
        model = Series
admin.site.register(Series, SeriesAdmin)


class EpisodeAdmin(admin.ModelAdmin):
    list_display = ['season', 'episode_number', 'sub_title', 'release_date']
    readonly_fields = ['episode_number']
    class Meta:
        model = Episode
admin.site.register(Episode, EpisodeAdmin)