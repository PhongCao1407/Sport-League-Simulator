from django.db import models

class Sport(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "sports"

    def __str__(self) -> str:
        return self.name