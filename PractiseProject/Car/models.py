from django.db import models
from Brand.models import Brand
# Create your models here.fr
class Post(models.Model):
    car_name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField(default=0)
    description = models.TextField()
    brand_name = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='posts/media/uploads/',blank=True,null=True)
    def __str__(self):
        return self.car_name

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comments by {self.name}"