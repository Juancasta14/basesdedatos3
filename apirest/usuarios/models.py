from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=80)
    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'usuarios'

class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='pedidos')
    producto = models.CharField(max_length=120)
    cantidad = models.IntegerField()

    class Meta:
        db_table = 'pedidos'  

class Perfil(models.Model):
    id = models.AutoField(primary_key=True)  
    nombre_perfil = models.CharField(max_length=100, unique=True) 

    class Meta:  
        db_table = 'perfilesJorge' 
      

    def _str_(self):
        return self.nombre_perfil 
                
        
class Usuario_jorge(models.Model):
    nombre_usuario = models.CharField(max_length=150)
    email_usuario = models.EmailField(unique=True)
    contrasena_usuario = models.CharField(max_length=255)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)

    class Meta:  
        db_table = 'usuariosJorge'
        
            
class Productos(models.Model):
    descripcion = models.CharField(max_length=80)
    stock = models.IntegerField()
    ubicacion = models.CharField(max_length=20)
    
    class Meta:
        db_table = 'productos_cristian'
        
        
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)  
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'clientesrocha'  

    def _str_(self):
        return self.nombre
