from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Vents(models.Model):

    MOOD_CHOICES = [
        ('vexed', 'Vexed'),
        ('stressed', 'Stressed'),
        ('tired', 'Tired'),
        ('broken', 'Broken'),
        ('calm', 'Calm'),
    ]

    CATEGORY_CHOICES = [
        ('traffic', 'Traffic Wahala'),
        ('work', 'Work Drama'),
        ('sapa', 'Sapa'),
        ('health', 'Health'),
        ('chaos', 'General Chaos'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='vents')
    title = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    mood = models.CharField(choices=MOOD_CHOICES, max_length=20, default='stressed')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='chaos')
    tension_level = models.IntegerField(default=50, validators=[
        MinValueValidator(1),
        MaxValueValidator(100),
    ],
    help_text='1 is chill, 100 is pure shege')

    is_anonymous = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username}'s vent on {self.created_at.strftime('%Y-%m-%d')}"