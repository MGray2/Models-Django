from django.test import TestCase
from app import models


# Create your tests here.


# test can create a friend
class TestFriends(TestCase):
    def test_can_create_friend(self):
        friend = models.add_friend("Phill", "McGraw", "1-800-999", True)

        self.assertEqual(friend.first_name, "Phill")
        self.assertEqual(friend.last_name, "McGraw")
        self.assertEqual(friend.phone_number, "1-800-999")
        self.assertEqual(friend.close_friend, True)

    # test can remove a friend
    def test_can_remove_friend(self):
        friends_list = [
            {
                first_name: "Barrack",
                last_name: "Obama",
                phone_number: "773-365-9687",
                close_friend: True,
            }
            {
                first_name: "Barcher",
                last_name: "Clash",
                phone_number: "100-808-4000",
                close_friend: False,
            }
            {
                first_name: "dog",
                last_name: "dont need one",
                phone_number: "im a dog",
                close_friend: True,
            }
        ]

        for individual in friends_list:
            models.add_friend(
                individual["name"],
                individual["email"],
                individual["phone"],
                individual["is_favorite"],
            )
        models.remove_friend("dog")
        self.assertEquals(len(models.show_all()), 2)