from django.db import models
from django.utils import timezone
from student.models import chatBase
from student.models import sbmtAssignment

# Create your models here.
class contact(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=30)
    email=models.EmailField()
    sub=models.CharField(max_length=20)
    msg=models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.fname} {self.lname}  ({self.sub}) "

class instructor(models.Model):
    name=models.CharField(max_length=60)
    image=models.ImageField(upload_to='instructor/images')
    about=models.TextField()
    qualifications=models.CharField(max_length=500)
    technologies=models.TextField()
    channel=models.URLField(null=True)
    def __str__(self):
        return f"{self.name} ({self.technologies}) " 

#batch notifications 
class bnotifications(models.Model):
    nTitle=models.CharField(max_length=20,default='Notification:',null=True)
    notification=models.TextField()
    nDate=models.DateField(default=timezone.now,null=True)
    def __str__(self):
        return self.nTitle

#Videos Model 
class video(models.Model):
    vTitle=models.CharField(max_length=100,default=None)
    vUrl=models.CharField(max_length=100)
    vDuration=models.DurationField()
    vDate=models.DateField(default=timezone.now)

    def videoSrc(self):
        return self.vUrl[17:]

    def __str__(self):
        return f"{self.vTitle} ({self.vDuration})"

#Assignmets model
class assignments(models.Model):
    name=models.CharField(max_length=100,default="Assignmet ")
    file=models.FileField(upload_to='assignment/given',default=None)
    submitDate=models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.name

#Enotes model 
class eNotes(models.Model):
    name=models.CharField(max_length=100)
    file=models.FileField(upload_to='student/batches/Notes')
    def __str__(self):
        return self.name
#study material model
class sMaterial(models.Model):
    name=models.CharField(max_length=30)
    about=models.TextField(default='For development purpose')
    image=models.ImageField(upload_to='StudyMaterial/images')
    file=models.FileField(upload_to='StudyMaterial/Files',default='StudyMaterial/Files/notAvailable.jpg')
    def __str__(self):
        return f"{self.name}"

# Batches model
class batch(models.Model):
    name = models.CharField(max_length=30,null=False)
    about = models.TextField(default='Not filled',max_length=500)
    
    icon = models.ImageField(upload_to='student/batches/images',null=True)
    bTime = models.DateField(default=timezone.now)
    bVideo = models.ManyToManyField(video,default=None)
    moreDescriptin=models.TextField(default='...')
    advantages=models.TextField(default='...')
    previewVideo=models.CharField(max_length=100,default='none')
    instructor=models.ForeignKey(instructor,on_delete=models.CASCADE,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField(default=0)
    notifications=models.ManyToManyField(bnotifications,default=None)
    timings=models.TimeField(default=timezone.now)
    assignments=models.ManyToManyField(assignments,blank=True)
    eNotes = models.ManyToManyField(eNotes,blank=True)
    def getLastAssign(sefl):
        return sefl.assignments.last()
    def previewSrc(self):
        return self.previewVideo[17:]
    
   

    def latestNotify(self):
        return self.notifications.last()
    
    def latestVideo(self):
        return self.bVideo.last()
    
    def discountedAmount(self):
        return (self.price * self.discount / 100)
    
    def finalPrice(self):
        return self.price - (self.price * self.discount / 100)
    
    def __str__(self):
        return f"{self.name}"



#signUp model 
class signUpModel(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.IntegerField()
    pswrd=models.CharField(max_length=20)
    sBatch=models.ManyToManyField("batch")
    image=models.ImageField(upload_to='student/images',default=None)
    address=models.CharField(max_length=100,null=True,default=None)
    qualification=models.CharField(max_length=20,null=True,default=None)
    college=models.CharField(max_length=50,null=True,default=None)
    submittedAssignment=models.ManyToManyField(sbmtAssignment, blank=True)
    pchats = models.ManyToManyField(chatBase,blank=True)
    def __str__(self) :
        return f"{self.fname} {self.lname} ({self.sBatch}) {self.image}"
    
