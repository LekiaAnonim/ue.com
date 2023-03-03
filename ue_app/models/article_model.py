from django.db import models
from ue_app.models.category_model import Category
from ue_app.models.channel_model import Channel
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
# Blog application imports.
from ue_app.utils.blog_utils import count_words, read_time
# Third party app imports
from taggit.managers import TaggableManager
# from ckeditor_uploader.fields import RichTextUploadingField
from tinymce import models as tinymce_models
from filebrowser.fields import FileBrowseField



class MediumInfo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(
        max_length=500, null=True, help_text='Enter the title of your post')
    slug = models.SlugField(null=True,  max_length=500)
    author = models.ForeignKey(Channel, on_delete=models.CASCADE)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    tags = TaggableManager(blank=True)

    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Publish'),
    )

    status = models.CharField(null=True,
        max_length=100, choices=STATUS_CHOICES, default='Draft')

    DISPLAY_CHOICE = (
        ('pr', 'Private'),
        ('pu', 'Public'),
    )

    display = models.CharField(
        max_length=100, choices=DISPLAY_CHOICE, default='Public')
    views = models.PositiveIntegerField(default=0)
    verify = models.BooleanField(default=False)
    

    @property
    def total_likes(self):
        return self.likes.count()
    

    class Meta:
        abstract = True
        ordering = ['-date_uploaded', 'author']

    


class Article(MediumInfo):
    feature_image = models.ImageField(null=True,
                                      default='article_image', upload_to="article_images")

    body = tinymce_models.HTMLField(null=True)
    count_words = models.CharField(max_length=50, default=0)
    read_time = models.CharField(max_length=50, default=0)
    likes = models.ManyToManyField(
        User, blank=True, related_name='ue_app_article_likes')

    @property
    def total_likes(self):
        return self.likes.count()

    @property
    def already_liked(self):
        user = self.author.profile.user
        if user.is_authenticated:
            if user in self.likes.all():
                liked = True
            else:
                liked = False
            return liked

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        self.count_words = count_words(self.body)
        self.read_time = read_time(self.body)
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('ue_app:article_detail', kwargs={'username': self.author.profile.user.username.lower(), 'slug': self.slug})

    def get_like_url(self):
        return reverse('ue_app:article_like_toggle', kwargs={'username': self.author.profile.user.username.lower(), 'slug': self.slug})

    def get_api_like_url(self):
        return reverse('ue_app:article_api_like_toggle', kwargs={'username': self.author.profile.user.username.lower(), 'slug': self.slug})
