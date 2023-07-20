from django.db.models import Model
from django.db.models import CharField
from django.db.models import ManyToManyField


# Create your models here.
class Participant(Model):
    id = CharField(max_length=100, primary_key=True)
    name = CharField(max_length=100)
    email = CharField(max_length=100, null=True)
    rooms = ManyToManyField('room.Room', related_name='participants')
