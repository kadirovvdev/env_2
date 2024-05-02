from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name


class Soccers(models.Model):

    category = models.ForeignKey(to="Category",on_delete=models.CASCADE)
    Position = models.CharField(max_length=100)
    number = models.IntegerField()
    body = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='soccers/', blank=True, null=True)


    class Meta:
        db_table = 'soccers'

    def __str__(self) -> str:
        return f"{self.category.name}, {self.Position}"


# Create your models here.
