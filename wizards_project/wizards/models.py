from django.db import models

# Create your models here.
class Wizard(models.Model):
    name = models.CharField(max_length=45)
    house = models.CharField(max_length=45) 
    pet = models.CharField(max_length=45)
    year = models.IntegerField()
        # define our own display for a Wizard object.
    def __repr__(self):
        return f"<Wizard object: ({self.id}) {self.name}, {self.house}, {self.pet}, {self.year} >\n"
