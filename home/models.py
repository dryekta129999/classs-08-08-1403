from django.db import models

# Create your models here.

class Post(models.Model):

	STATUS_CHOICES = (
		('published', 'published'),
		('draft', 'draft'),

	)

	title = models.CharField(max_length=100,null=False)
	content = models.TextField(max_length=1000,null=True,blank=True)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')


	def __str__(self):
		return self.title
