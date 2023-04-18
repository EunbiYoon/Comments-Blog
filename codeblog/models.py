from django.db import models

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=255)
    slug=models.SlugField()
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural='Categories'

class Post(models.Model):
    category=models.ForeignKey(Category, related_name='post_model', on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    slug=models.SlugField()
    intro=models.TextField()
    body=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post=models.ForeignKey(Post, related_name='comment_model', on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    body=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '%s - %s' % {self.post.title, self.name}
    