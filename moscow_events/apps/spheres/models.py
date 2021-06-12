from django.db import models


class Sphere(models.Model):
    sphere_name = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.sphere_name}'
