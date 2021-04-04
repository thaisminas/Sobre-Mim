from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField('Titulo', max_length=255)
    slug = models.SlugField('Slug', max_length=255, unique=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField('Conteudo')
    created = models.DateTimeField('criado', auto_now_add=True)
    updated = models.DateTimeField('atualizado', auto_now=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})



