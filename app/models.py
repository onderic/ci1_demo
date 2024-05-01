from django.db import models

# Create your models here.

class DisciplinaryCase(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Add more fields as needed

    def __str__(self):
        return self.title

class Notification(models.Model):
    user = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # Add more fields as needed

    def __str__(self):
        return self.message
    
class Document(models.Model):
    case = models.ForeignKey(DisciplinaryCase, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='documents/')
    created_at = models.DateTimeField(auto_now_add=True)
    # Add more fields as needed

    def __str__(self):
        return self.title

