from django.db import models

# Create your models here.

tipo_envio= [
    [0 ,'domicilio'],
    [1 , 'retiro'],
    [2, 'express'],
]

estado=[
    [0 ,'Recibido'],
    [1 , 'Traslado'],
    [2, 'Reparto'],
    [3,'Entregado'],
    [4, 'Sin Informacion'],
]


class Cliente (models.Model):
    
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    rut=models.IntegerField()
    direccion=models.CharField(max_length=20)
    num_telf=models.IntegerField()
    email= models.EmailField()

    def __str__(self):
       return self.rut

class Encomienda(models.Model):
    cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    num_env=models.AutoField(primary_key=True)
    origen=models.CharField(max_length=20)
    destino=models.CharField(max_length=20)
    tipo_env=models.IntegerField(choices=tipo_envio)
    destinatario=models.CharField(max_length=20)
    rut_dest=models.IntegerField()
    contacto_dest=models.IntegerField()
    
    def __str__(self):
        return self.num_env
    
class Seguimiento(models.Model):
    codigo=models.ForeignKey(Encomienda, on_delete=models.CASCADE)
    estado=models.IntegerField(choices=estado)
     
    def __str__(self):
        return self.estado 
    