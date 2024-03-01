from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255, db_index = True)
    author = models.CharField(max_length=100, db_index = True)
    description = models.TextField(null=True, blank=True)
    isbn = models.CharField(max_length=20, unique=True)
    published_date = models.DateField(null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
