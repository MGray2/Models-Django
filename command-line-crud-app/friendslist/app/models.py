from django.db import models


# Create your models here.
class Friend(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    close_friend = models.BooleanField()


def add_friend(first_name, last_name, phone_number, close_friend):
    new_friend = Friend(
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number,
        close_friend=close_friend,
    )
    new_friend.save()
    return new_friend


def remove_friend(first_name):
    friend_to_delete = Friend.objects.get(first_name=first_name)
    friend_to_delete.delete()
    return friend_to_delete


def show_all():
    return Friend.objects.all()


def find_by_name(name):
    try:
        return Friend.objects.filter(first_name=name)
    except:
        return Friend.objects.filter(last_name=name)


def show_close_friends():
    return Friend.objects.filter(close_friend=True)


def change_close_status(name, status):
    try:
        person = Friend.object.get(first_name=name)
        if len(person) != 0:
            person.close_friend = status
            person.save()
            return person
    except:
        person = Friend.object.get(last_name=name)
        if len(person) != 0:
            person.close_friend = status
            person.save()
            return person
