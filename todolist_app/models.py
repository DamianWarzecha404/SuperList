from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tasklist (models.Model):     #dodajemy pierwsze zadanie i robimy Migration + migrate(by zrobić upload)
    id = models.AutoField(primary_key=True)
    owner= models.ForeignKey(User, on_delete=models.CASCADE, default=None) # dodajemy Ownera, dzięki temu tylko Owner zadania bedzie mógł je edytować/usuwać. (robimy też migrations i migrate by zmiana zadziała na serwerze)
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)


    class Meta:
        ordering = ['id']


    def __str__(self):    # dzieki temu będziemy widzieć nasze Taski w przegladarce, a nie jako Object #1 , Object #2
        return self.task + " - " + str(self.done)