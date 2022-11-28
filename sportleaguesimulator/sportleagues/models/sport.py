from django.db import models

class Sports(models.Model):
    name = models.CharField(primary_key=True, max_length=100)

    class Meta:
        managed = True
        db_table = 'sports'
    

def __str__(self):
    return self.name