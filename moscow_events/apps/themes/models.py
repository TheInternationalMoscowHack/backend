from django.db import models


class Theme(models.Model):
    theme_name = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.theme_name}'
