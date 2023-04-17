from django.db import models
from django.utils import timezone
import os

# Create your models here.
class Upload(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    file = models.FileField(upload_to='documents/',null=True)

    def __str__(self):
        return self.name
    
    def extension(self):
        name, extension = os.path.splitext(self.file.name)
        return extension
    
    def filesize(self):
        size = os.path.getsize(self.file.name)
        suffixes = ['B', 'KB', 'MB', 'GB', 'TB']
        i = 0
        while size >= 1024 and i < len(suffixes)-1:
            size /= 1024
            i += 1
        return f"{size:.2f} {suffixes[i]}"