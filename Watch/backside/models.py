from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.db.models import Max

# Create your models here.


class Category(models.Model):
    genre = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.genre
    
from django.contrib.auth.models import User

# Subscription model
from django.utils.timezone import now, timedelta


class Plan(models.Model):
    FREE = 'free'
    PREMIUM = 'premium'
    FAMILY = 'family'
    STUDENT = 'student'

    PLAN_CHOICES = [
        (FREE, 'Free'),
        (PREMIUM, 'Premium'),
        (FAMILY, 'Family'),
        (STUDENT, 'Student'),
    ]

    name = models.CharField(max_length=20, choices=PLAN_CHOICES, unique=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Fixed price for each plan

    def __str__(self):
        return f"{self.name.capitalize()} (${self.cost})"


class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='subscription')
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(blank=True, null=True)  # Lifetime for admin; one month for others.

    def save(self, *args, **kwargs):
        # Automatically assign lifetime Premium to admin users
        if self.user.is_staff:  # Admin users
            self.plan = Plan.objects.get(name=Plan.PREMIUM)
            self.end_date = None  # Lifetime subscription
        else:
            # For other users, set an end date of one month from now
            if not self.end_date:  # Only set if end_date isn't already specified
                self.end_date = now().date() + timedelta(days=30)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.plan.name.capitalize()}"

class Series(models.Model):
    MOVIE = 'movie'
    SEASON = 'season'
    TYPE_CHOICES = [
        (MOVIE, 'Movie'),
        (SEASON, 'Season'),
    ]
    title = models.CharField(max_length=255)
    genreOne = models.ForeignKey('Category', related_name='series1', on_delete=models.CASCADE, blank=True, default='action')
    genreTwo = models.ForeignKey('Category', related_name='series2', on_delete=models.CASCADE, blank=True, default='action')
    genreThree = models.ForeignKey('Category', related_name='series3', on_delete=models.CASCADE, blank=True, default='action')
    description = models.TextField()
    release_date = models.DateField()
    poster = models.ImageField(upload_to='series_posters/', null=True, blank=True)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default=SEASON)  # Movie or Season
    season_number = models.PositiveIntegerField(null=True, blank=True)  # Only relevant for seasons
    premium_only = models.BooleanField(default=False)  # Accessible to premium users only

    def save(self, *args, **kwargs):
        # Automatically assign a season number for seasons
        if self.type == self.SEASON and not self.pk:  # New season entry
            max_season_number = Series.objects.filter(
                type=self.SEASON
            ).aggregate(Max('season_number'))['season_number__max']
            self.season_number = 1 if max_season_number is None else max_season_number + 1

        # Ensure movies do not have a season number
        if self.type == self.MOVIE:
            self.season_number = None

        super().save(*args, **kwargs)

    def __str__(self):
        if self.type == self.MOVIE:
            return f"{self.title} (Movie)"
        return f"{self.title} - Season {self.season_number}"
    
# Episode model
class Episode(models.Model):
    season = models.ForeignKey("Series", on_delete=models.CASCADE, related_name='episodes')
    episode_number = models.PositiveIntegerField(editable=False)  # Automatically assigned
    sub_title = models.CharField(max_length=255)
    release_date = models.DateField()
    videos = models.FileField(null=True, blank=True, upload_to="anime_video/")  # Video file upload path
    duration_minutes = models.PositiveIntegerField(editable=False, null=True, blank=True)  # Auto-extracted

    def save(self, *args, **kwargs):
        # Automatically assign an episode_number within the season
        if not self.pk:  # Only assign on creation
            max_episode_number = Episode.objects.filter(season=self.season).aggregate(Max('episode_number'))['episode_number__max']
            self.episode_number = 1 if max_episode_number is None else max_episode_number + 1

        # Enforce the 'movie' type constraint
        if self.season.type == 'movie' and Episode.objects.filter(season=self.season).exists():
            raise ValueError("A 'movie' type season can only have one episode.")

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.season.title} - S{self.season.season_number}E{self.episode_number}: {self.sub_title}"
