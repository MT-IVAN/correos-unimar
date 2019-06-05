from django.db import models

# Create your models here.

class Formulario(models.Model):
	ASUNTO = (
        ('Peticiòn', 'Peticiòn'),
        ('Queja', 'Queja'),
        ('Reclamo', 'Reclamo'),
    )
	nombre = models.CharField(max_length=30)
	correo = models.EmailField()
	asunto = models.CharField(choices=ASUNTO, max_length=30)
	mensaje = models.CharField(max_length=30)