from rest_framework.serializers import ModelSerializer
from .models import  *

class personneserializer(ModelSerializer):
    class Meta:
        model=personne
        fields = '__all__'

class usersserializer(ModelSerializer):
    class Meta:
        model=users
        fields = '__all__'

class locationserializer(ModelSerializer):
    class Meta:
        model=location
        fields = '__all__'

class mealserializer(ModelSerializer):
    class Meta:
        model=meal
        fields = '__all__'

class menuserializer(ModelSerializer):
    class Meta:
        model=menu
        fields = '__all__'

class restaurantserializer(ModelSerializer):
        class Meta:
            model = restaurant
            fields = '__all__'
class avisserializer(ModelSerializer):
    class Meta:
        model=avis
        fields = '__all__'