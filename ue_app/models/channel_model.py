from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(
        User, null=True, related_name="account", on_delete=models.CASCADE)
    middle_name = models.CharField(
        max_length=200, blank=True, null=True, help_text="Enter your middle name")
    photo = models.ImageField(default="avatar.png",
                              upload_to="profile_picture", null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    phone_number = models.CharField(
        max_length=12, null=True, help_text="Enter your State or Phone Number")
    address = models.CharField(
        max_length=500, blank=True, null=True, help_text="Enter your House address")
    city = models.CharField(
        max_length=100, help_text="Enter your City (e.g. Lagos)", null=True, blank=True)
    region = models.CharField(
        max_length=100, help_text="Enter your State or Region (e.g. Rivers)", null=True, blank=True)
    country = models.CharField(
        max_length=100, help_text="Enter your Country (e.g. Nigeria)", null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"@{self.user.username}"

    def get_absolute_url(self):
        return reverse('ue_app:customer-update', kwargs={'pk': self.pk})

class Channel(models.Model):
    profile = models.ForeignKey(Profile, null=True, related_name="channel", on_delete=models.SET_NULL)
    display_name = models.CharField(
        max_length=200, blank=True, null=True, help_text="Enter the name of your channel")
    banner = models.ImageField(default="banner.png",
                              upload_to="channel_banner", null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"@{self.display_name}"
