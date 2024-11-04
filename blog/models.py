from django.db import models
from django.contrib.auth.models import User

# Create your models here.


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
    # tag
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
