from django.db import models
class personne(models.Model):
    name=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)
    mail=models.EmailField()
    birthday=models.DateField()
    pid=models.IntegerField(primary_key=True)
    location_id=models.IntegerField()

    def __str__(self):
        return (self.name+self.lastname)

class  users(models.Model):
    username= models.CharField(max_length=30)
    password= models.CharField(max_length=30)
    permission= models.BinaryField()
    pid=models.ForeignKey(personne, on_delete=models.CASCADE)
    uid=models.IntegerField(primary_key=True)

#class users(models.Model,users):
class location(models.Model):
    location_id=models.IntegerField(primary_key=True)
    postal_code=models.IntegerField()
    country= models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    city =models.CharField(max_length=30)







class meal(models.Model):
     meal_id=models.IntegerField(primary_key=True)
     name=models.CharField(max_length=30)
     price=models.FloatField()
     picture=models.ImageField()
     description=models.CharField(max_length=30)

class menu(models.Model):
    menu_id = models.IntegerField(primary_key=True)
    meal_id = models.ForeignKey(meal, on_delete=models.CASCADE)

class restaurant(models.Model):
    name=models.CharField(max_length=30)
    mail=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)
    description=models.CharField(max_length=30)
    restaurant_id=models.IntegerField(primary_key=True)
    location_id=models.ForeignKey(location, on_delete=models.CASCADE)
    avis_id=models.IntegerField()
    menu_id=models.ForeignKey(menu, on_delete=models.CASCADE)
    #categorie


class avis(models.Model):
    avis_id=models.IntegerField(primary_key=True)
    rating=models.FloatField()
    commentaire=models.CharField(max_length=30)
    restaurant_id=models.ForeignKey(restaurant, on_delete=models.CASCADE)
    uid=models.ForeignKey(users, on_delete=models.CASCADE)
    username=models.CharField(max_length=30)





