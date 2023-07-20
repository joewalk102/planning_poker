from django.db.models import Model
from django.db.models import BooleanField
from django.db.models import CharField


# Create your models here.
class Room(Model):
    name = CharField(max_length=100)
    locked = BooleanField(default=False)
