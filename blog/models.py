from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from ckeditor.fields import RichTextField


class Category(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name



class Post(models.Model):
	title = models.CharField(max_length=100)
	date_posted = models.DateTimeField(default=timezone.now)
	excerpt = models.TextField(default=None)
	content = RichTextField(blank=True, null=True)
	hero_image = models.ImageField(default=None, upload_to='media')
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.PROTECT, default=None)

	must_read = models.BooleanField(default=False)
	favorite = models.BooleanField(default=False)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url