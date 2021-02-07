from django.db import models

# Create your models here
# this use for handle the data base
# and use the class the for handle categories or attribute
#
#
# create categories model.
""" Model is a class in which it contain some property and this property can use by the models class now 
#this title function variable use for to give the name of model categories in character and max_length with 100 character
# this is use to describe what is the title field to be a textfield or any thing else"""


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


# create image madel


class Image(models.Model):
    """ #model is the parent class here for Image class #now we take attributes that thing will describe the image (like title, description ,image,added date etc)"""

    title = models.CharField(max_length=200)
    description = models.TextField()

    # actual image to folder images

    image = models.ImageField(upload_to='images')
    added_date = models.DateTimeField()
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
