from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # (User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'blog/', default = 'blog/default.jpg')
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    tag = TaggableManager()
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta():
        ordering = ["created_date"]
        verbose_name = "post"


    def __str__(self):          # To see id numbers at the same time 
        return self.title  # return " {} - {} ".format(self.title,self.id)
    
    def __add__(self, other):
        if isinstance(other, int):
            self.counted_view += other
            self.save()
        return self
    
    def snippest(self):
        return self.content[:100] + '...'
    
    def get_absolute_url(self):
        return reverse('blog:single',kwargs={'pid':self.id})


class Comment(models.Model):
    post = models.ForeignKey(post,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):          
        return self.name
    