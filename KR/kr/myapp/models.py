from django.db import models

# Create your models here.
class UsersManager(models.Manager):
    
    def get_users_by_name(self, name):
        return self.filter(name_full=name)

    def get_users_by_city(self, city):
        return self.filter(realty__city=city).distinct()

    def get_active_users(self):
        return self.filter(is_active=True)

    def get_admin_users(self):
        return self.filter(is_staff=True, is_superuser=True)



class RealtyManager(models.Manager):
    def get_realty_by_type(self, realty_type):
        return self.filter(type=realty_type)

    def get_realty_by_city(self, city):
        return self.filter(city=city)

    def get_realty_by_user(self, user_id):
        return self.filter(user=user_id)

    def get_expensive_realty(self):
        return self.filter(price__gt=1000000)

    def get_cheapest_realty(self):
        return self.filter(price__lt=50000)



class FavoritesManager(models.Manager):
    def get_favorites_by_user(self, user_id):
        return self.filter(user=user_id)

    def get_favorites_by_realty(self, realty_id):
        return self.filter(realty=realty_id)

class Users(models.Model):
    name_full = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    manager = UsersManager()
    
class Realty(models.Model):
    type = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    square = models.CharField(max_length=13)
    price = models.CharField(max_length=13)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    manager = RealtyManager()

class Favorites(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    realty = models.ForeignKey(Realty, on_delete=models.CASCADE)
    manager = FavoritesManager()

