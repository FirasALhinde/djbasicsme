from django.utils import timezone
from distutils.command.upload import upload
from email.mime import image
from django.db import models

# Create your models here.





class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=10000,null=True,blank=True )
    publish_date = models.DateField(default=timezone.now)
    update_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='posts/')
    category =models.ForeignKey('Category',on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name ='My Post'
        ordering = ['-publish_date']
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Categories"
