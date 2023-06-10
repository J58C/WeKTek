from django.db import models

class Code(models.Model):
    language = models.CharField(max_length=50)
    code = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
