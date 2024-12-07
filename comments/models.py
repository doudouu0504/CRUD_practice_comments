from django.db import models
from resumes.models import Resume


class Comments(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)


# Create your models here.
