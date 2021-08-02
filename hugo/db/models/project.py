from django.db import models
from.user import User

class Project(models.Model):

    assignee = models.ForeignKey(User, on_delete=models.CASCADE)
    client =  models.CharField( max_length=100, blank=True, null=True)
    name =  models.CharField( max_length=100, blank=True, null=True)
    description =  models.CharField( max_length=100, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Project"
        db_table = "project"

    def __str__(self):
        return self.assignee