from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import CustomUser

# Create your models here.


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('Web Development', 'Web Development'),
        ('Graphic Design', 'Graphic Design'),
        ('Content Writing', 'Content Writing'),
        ('Digital Marketing', 'Digital Marketing'),
        ('Mobile App Development', 'Mobile App Development'),
        ('Video Editing', 'Video Editing'),
    ]

    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posted_projects', null=True, blank=True)
    company_name = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=200,null=True)
    description = models.TextField(default="No description")
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    skills = models.CharField(max_length=200, null=True, blank=True)  
    budget_min = models.IntegerField(null=True, blank=True)
    budget_max = models.IntegerField(null=True, blank=True)
    deadline = models.CharField(max_length=50, null=True, blank=True) 
  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Proposal(models.Model):
    freelancer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='proposals')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='proposals')
    message = models.TextField()
    proposed_budget = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.freelancer.get_full_name()} -> {self.project.title}"
    



class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    skills = models.CharField(max_length=300)
    budget = models.FloatField()
    deadline = models.DateField()
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title