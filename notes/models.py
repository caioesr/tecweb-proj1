from django.db import models

class Tag(models.Model):
    tag = models.CharField(max_length=30)
    label = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.tag}'

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.id}.{self.title}'