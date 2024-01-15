from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200, default='')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    year = models.IntegerField(default=0)
    cover_url = models.URLField(default='')
    available_in_pdf = models.BooleanField(default=False)
    pdf_url = models.URLField(default='', null=True, blank=True)
    available_in_epub = models.BooleanField(default=False)
    epub_url = models.URLField(default='', null=True, blank=True)

    def __str__(self):
        return self.title
