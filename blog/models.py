from django.db import models

# Create your models here.

class post(models.Model):
    # author
    # image
    title = models.CharField(max_length=255)
    content = models.TextField()
    # category = models.IntegerField()
    # tag
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):          # To see id numbers at the same time 
        return self.title       # return " {} - {} ".format(self.title,self.id)