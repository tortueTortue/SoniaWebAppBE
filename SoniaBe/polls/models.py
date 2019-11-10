from django.db import models

# Create your models here.


class ModuleName(models.Model):
    name = models.CharField(max_length=150)
    icon = models.CharField(default="cellphone-link", max_length=50)


class Layout(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Module(models.Model):
    name = models.ForeignKey(ModuleName, on_delete=models.DO_NOTHING)
    belongsToLayout = models.ForeignKey(Layout, on_delete=models.DO_NOTHING)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    h = models.IntegerField(default=0)
    w = models.IntegerField(default=0)
    isResizable = models.BooleanField(default=True)
    isDraggable = models.BooleanField(default=True)
    isStatic = models.BooleanField(default=False)
