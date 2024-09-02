from django.db import models

"""Models are classes  in python. They are just blueprints (schemas) to make database tables.

Eg. To create a model student, simple create a class named Student"""

class Item(models.Model):

    ##format the output when we run Item.object.all()
    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://archive.org/download/placeholder-image/placeholder-image.jpg")
