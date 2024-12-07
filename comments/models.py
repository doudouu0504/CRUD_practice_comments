from django.db import models
from resumes.models import Resume
from django.utils import timezone


class Comments(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, db_index=True)

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()


# Create your models here.
