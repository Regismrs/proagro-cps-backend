from django.db import models

class Evento (models.Model):
    nome = models.CharField(max_length=30, null=False)

    def __str__(self):
        return str(self.id) + '-' + self.nome
    
class ComunicadoCliente (models.Model):
    id = models.AutoField(primary_key = True, auto_created=True)
    cpf = models.CharField(max_length=11, null=False)
    nome = models.CharField(max_length=80, null=False)
    email = models.EmailField(max_length=100, null=False)
    evento = models.ForeignKey(Evento, on_delete=models.PROTECT, related_name="evento")
    lavoura_lat = models.FloatField(null=False)
    lavoura_lon = models.FloatField(null=False)
    lavoura_tipo = models.SmallIntegerField(null=False)
    lavoura_data_colheita = models.DateTimeField()
    inserted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.nome + " - " + self.cpf
