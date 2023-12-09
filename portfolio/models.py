from django.db import models
import uuid
# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    proj_link = models.TextField(max_length=2000, blank=True, null=True)
    source_link = models.TextField(max_length=2000, blank=True, null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_totals = models.IntegerField(default=0, blank= True, null= True)
    vote_ratio = models.IntegerField(default=0 ,blank= True, null= True)
    added_time = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    
    def __str__(self): 
        return self.title  

class Review(models.Model):
    # owners =
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    Vote_Type = (
        ('up', 'Up Vote'),
        ('down', 'down Vote')
    )
    body =models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=Vote_Type)
    added_time = models.DateTimeField(auto_now_add=True)

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
       return  self.value
        
class Tag(models.Model):
      name = models.CharField(max_length=200)
      added_time = models.DateTimeField(auto_now_add=True)
      id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
      def __str__(self):
         return  self.name