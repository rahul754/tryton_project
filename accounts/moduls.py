from django.db import models

class AuthProfile(models.Model):
    tryton_id = models.IntegerField(
        null=True,
        blank=True,
    )
