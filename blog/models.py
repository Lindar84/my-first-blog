from django.db import models

# Create your models here.
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(                     # ukazuje na jinou tabulku
        'auth.User', on_delete=models.CASCADE)      # pokud se smaze autor, smaze vse, co s nim souvisi
    tittle = models.CharField(max_length=200)       # text o max. delce 200 znaku
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(          # pokud clanek jeste nechci publikovat
        blank=True, null=True)                      # toto pole muze byt prazdne

# metody pro tuto tridu:
    def publish(self):
        self.published_date = timezone.now()        # zapise se do pameti PC
        self.save()                                 # zapise do databaze

    def __str__(self):                              # jak se prevede prispevek na retezec
        return self.tittle

# zmena modelu se dela pri vyple databazi

