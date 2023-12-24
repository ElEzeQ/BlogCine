from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.



class Categoria(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    
    def __str__(self) -> str:
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    subtitulo = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    texto = RichTextField(null=False)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, default="Sin categoría")
    imagen = models.ImageField(null=True, blank=True, upload_to="posts/img", default="static/img/post_default.png")
    publicado = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ("-publicado",)

    def comentarios_realizados(self):
        return self.comentario_set.all()


    def __str__(self):
        return self.titulo
    
    def delete(self, using = None, keep_parents = False):
        self.imagen.delete(self.imagen.name)
        super().delete()

class Comentario(models.Model):
    texto = models.TextField(null= False)
    fecha = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.post} {self.texto}"