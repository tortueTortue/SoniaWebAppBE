from django.db import models

# Create your models here.

class ModuleName(models.Model):
    name = models.CharField(max_length=150)

class ModuleList(models.Model):
    listName = models.ForeignKey(ModuleName, on_delete=models.DO_NOTHING)

class Layout(models.Model):
    name = models.CharField(max_length=50)
    modules = models.ForeignKey(ModuleList, on_delete=models.CASCADE)

class Module(models.Model):
    name = models.ForeignKey(ModuleName, on_delete=models.DO_NOTHING)
    belongsToList = models.ForeignKey(ModuleList, on_delete=models.DO_NOTHING)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    h = models.IntegerField(default=0)
    w = models.IntegerField(default=0)
    isResizable = models.BooleanField(default=True)
    isDraggable = models.BooleanField(default=True)
    isStatic = models.BooleanField(default=False)    