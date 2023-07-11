from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()
    categories = models.ManyToManyField('Category')
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Add validation to ensure the event date is in the future
        # You can also include other custom validations here
        # For example:
        if self.date < timezone.now().date():
            raise ValidationError("Event date must be in the future.")
        super(Event, self).save(*args, **kwargs)

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.event.title}"

class Venue(models.Model):
    name = models.CharField(max_length=255)
    capacity = models.IntegerField()
    amenities = models.TextField()
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name