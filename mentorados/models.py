from django.db import models
from django.contrib.auth.models import User

class Navigators(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentorados_navigators') 

    def __str__(self):
        return self.nome

class Mentorados(models.Model):
    estagio_choice = (
        ('1', '10-100k'),  
        ('2', '100-1kk'),  
    )

    nome = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='foto', null=True, blank=True)
    estagio = models.CharField(max_length=1, choices=estagio_choice)
    navigator = models.ForeignKey(Navigators, null=True, blank=True, on_delete=models.CASCADE )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentorados_mentorados')
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome

