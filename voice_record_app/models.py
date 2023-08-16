from django.db import models

# Create your models here.
class Domaine(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Audio(models.Model):
    domaine = models.ForeignKey(Domaine, on_delete=models.CASCADE)
    audio = models.FileField(upload_to='audio_files/')
    date = models.DateTimeField()
    auteur = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.domaine} - {self.auteur}"
