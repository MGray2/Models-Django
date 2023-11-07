from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    is_favorite = models.BooleanField()

    def __str__(self):
        return self.name


def create_contact(name, email, phone, is_favorite):
    new_contact = Contact(name=name, email=email, phone=phone, is_favorite=is_favorite)
    new_contact.save()
    return new_contact


def all_contacts():
    return Contact.objects.all()


def find_contact_by_name(name):
    try:
        return Contact.objects.get(name=name)
    except:
        return None


def favorite_contacts():
    return Contact.objects.filter(is_favorite=True)


def update_contact_email(name, new_email):
    person = Contact.objects.get(name=name)
    person.email = new_email
    person.save()
    return person


def delete_contact(name):
    to_remove = Contact.objects.get(name=name)
    to_remove.delete()
    return to_remove
