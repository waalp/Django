from django.db import models
import uuid
import os


# Create your models here.

def user_directory_path(instance,filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10],ext)
    return os.path.join(instance.username,'headimg',filename)

class User(models.Model):
    username = models.CharField(max_length=30)
    headimg = models.FileField(upload_to=user_directory_path,verbose_name='头像',blank=True)
    password = models.CharField(max_length=256)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reversed('blog:pic_detail',args=[str(self.id)])

class Blog(models.Model):
    title = models.CharField(max_length=256)
    art = models.CharField(max_length=1024)