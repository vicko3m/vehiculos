from django.db import models

class Vehiculo(models.Model):
    MARCAS = [
        ('Fiat', 'Fiat'),
        ('Chevrolet', 'Chevrolet'),
        ('Ford', 'Ford'),
        ('Toyota', 'Toyota'),
        ('Honda', 'Honda'),
        ('Volkswagen', 'Volkswagen'),
        ('Nissan', 'Nissan'),
        ('Hyundai', 'Hyundai'),
    ]
    
    CATEGORIAS = [
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga'),
        ('Comercial', 'Comercial'),
    ]

    marca = models.CharField(
        max_length=20, 
        choices=MARCAS,
        verbose_name='Marca'
    )
    modelo = models.CharField(
        max_length=100,
        verbose_name='Modelo'
    )
    serial_carroceria = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Serial de Carrocería'
    )
    serial_motor = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Serial del Motor'
    )
    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIAS,
        verbose_name='Categoría'
    )
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Precio'
    )
    fecha_registro = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de Registro'
    )
    año = models.IntegerField(
        verbose_name='Año',
        help_text='Año del vehículo'
    )
    
    class Meta:
        verbose_name = 'Vehículo'
        verbose_name_plural = 'Vehículos'
        ordering = ['-fecha_registro']

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.serial_carroceria}"