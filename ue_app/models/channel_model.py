from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify


class Profile(models.Model):
    user = models.OneToOneField(
        User, null=True, related_name="account", on_delete=models.CASCADE)
    first_name = models.CharField(
        max_length=200, blank=True, null=True, help_text="Enter your first name")
    last_name = models.CharField(
        max_length=200, blank=True, null=True, help_text="Enter your last name")
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
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"@{self.user.username}"

    def get_absolute_url(self):
        return reverse('ue_app:profile_detail', kwargs={'username': self.profile.user.username.lower(), 'pk': self.pk})


class Channel(models.Model):
    profile = models.ForeignKey(
        Profile, null=True, related_name="channel", on_delete=models.SET_NULL)
    display_name = models.CharField(
        max_length=200, blank=True, null=True, help_text="Enter the name of your channel")
    slug = models.SlugField(null=True,  max_length=500)
    banner = models.ImageField(default="banner.png",
                               upload_to="channel_banner", null=True, blank=True)
    channel_logo = models.ImageField(default="channel.png",
                                     upload_to="channel_logo", null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)
    follow = models.ManyToManyField(
        User, blank=True, related_name="follow")

    def __str__(self):
        return f"@{self.display_name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.display_name, allow_unicode=True)

        super(Channel, self).save(*args, **kwargs)

    @property
    def already_following(self):
        user = self.profile.user
        if user.is_authenticated:
            if user in self.follow.all():
                following = True
            else:
                following = False
            return following

    def get_absolute_url(self):
        return reverse('ue_app:channel_detail', kwargs={'username': self.profile.user.username.lower(), 'slug': self.slug})

    def get_follow_url(self):
        return reverse('ue_app:channel_follow_toggle', kwargs={'username': self.profile.user.username.lower(), 'slug': self.slug})

    def get_api_follow_url(self):
        return reverse('ue_app:channel_api_follow_toggle', kwargs={'username': self.profile.user.username.lower(), 'slug': self.slug})