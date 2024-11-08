from django.db import models
from django.utils import timezone

from apps.user.models import User

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=120)  # nombre_apellido
    email = models.EmailField() # correo electronico
    subject = models.CharField(max_length=50)  # asunto
    message = models.TextField()  # mensaje
    date = models.DateTimeField(default=timezone.now)  # fecha

    class Meta():
        ordering = ('-date',)

    def __str__(self):
        return self.full_name  # nombre_apellido


