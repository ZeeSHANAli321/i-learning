from django.db import models
from django.utils import timezone
import os
from user.models import *

#submitted assignments for student model 
class sbmtAssignment(models.Model):
    assignmentId=models.CharField(max_length=100,null=True)
    name=models.CharField(max_length=100,default="Student Assignment")
    #file=models.FileField(upload_to='student/submitAssignments')
    date=models.DateField(default=timezone.now)
    
    def custom_file_name(instance, filename):
        # Get the user's username (or any other unique identifier)
        
        username = instance.name
        date=instance.date

        # Extract the file extension from the original filename
        file_extension = os.path.splitext(filename)[1]

        # Create a filename based on the user's username and timestamp
        new_filename = f'{username}_{date}_{file_extension}'

        return os.path.join('student/submitAssignments', new_filename)

    file = models.FileField(upload_to=custom_file_name,null=False)
    def __str__(self):
        return self.name

class thoughts(models.Model):
    thoughtOfDay=models.CharField(max_length=300)
    def __str__(self):
        return self.thoughtOfDay
    
class complaint(models.Model):
    email=models.CharField(max_length=50)
    complain=models.TextField()
    def __str__(self):
        return self.email
    
#Doubt solver ai chats Models
class chat(models.Model):
    query = models.TextField(null=True)
    responce = models.TextField(null=True)
    def __str__(self):
        return self.query
    

class chatBase(models.Model):
    name = models.TextField(default="Could not load title" , max_length=50)
    date = models.DateField(default=timezone.now)
    chats = models.ManyToManyField("chat",blank=True)
    def __str__(self):
        return self.name
    
    