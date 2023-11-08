from django.db import models


# Create your models here.
class Friend(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    close_friend = models.BooleanField()


# adding friends
def add_friend(first_name, last_name, phone_number, close_friend):
    new_friend = Friend(
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number,
        close_friend=close_friend,
    )
    new_friend.save()
    return new_friend


# removing friends
def remove_friend(first_name):
    friend_to_delete = Friend.objects.get(first_name=first_name)
    friend_to_delete.delete()
    return friend_to_delete


# display all friends
def show_all():
    return Friend.objects.all()


# search by full name
def find_by_name(fname, lname):
    try:
        return Friend.objects.get(first_name=fname, last_name=lname)
    except:
        return None


# show only close friends
def show_close_friends():
    return Friend.objects.filter(close_friend=True)


# update close status
def change_close_status(name, status):
    person = Friend.objects.get(first_name=name)
    person.close_friend = status
    person.save()
    return person
