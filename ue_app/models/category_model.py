from django.db import models


class Category(models.Model):
    """
    The Category model, is a model of posts category type for all medium type (i.e. Article, Audio, Video).
    """
    name = models.CharField(max_length=100, help_text='Select or Enter your Post category e.g. Travel')
    slug = models.SlugField(max_length=100)
    image = models.ImageField(
                              upload_to="category_image", null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('ue_app:category_detail',
                       kwargs={'slug': self.slug})
