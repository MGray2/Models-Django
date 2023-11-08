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

    # test can see all friends
    def test_view_all_friends(self):
        friends_list = [
            {
                "first_name": "Barack",
                "last_name": "Obama",
                "phone_number": "07-854-839",
                "close_friend": True,
            },
            {
                "first_name": "Doc",
                "last_name": "Louis",
                "phone_number": "014-213-8118",
                "close_friend": True,
            },
            {
                "first_name": "Dog",
                "last_name": "Dont have one",
                "phone_number": "Dont need one",
                "close_friend": False,
            },
        ]

        for friend in friends_list:
            models.add_friend(
                friend["first_name"],
                friend["last_name"],
                friend["phone_number"],
                friend["close_friend"],
            )

        all_friends = models.show_all()
        self.assertEqual(len(all_friends), len(friends_list))
        friends_list = sorted(friends_list, key=lambda c: c["first_name"])
        all_friends = sorted(all_friends, key=lambda c: c.first_name)

        for data, friend in zip(friends_list, all_friends):
            self.assertEqual(data["first_name"], friend.first_name)
            self.assertEqual(data["last_name"], friend.last_name)
            self.assertEqual(data["phone_number"], friend.phone_number)
            self.assertEqual(data["close_friend"], friend.close_friend)

    # specific friend search
    def test_search_for_specific_friend(self):
        friends_list = [
            {
                "first_name": "Barack",
                "last_name": "Obama",
                "phone_number": "07-854-839",
                "close_friend": True,
            },
            {
                "first_name": "Doc",
                "last_name": "Louis",
                "phone_number": "014-213-8118",
                "close_friend": True,
            },
            {
                "first_name": "Dog",
                "last_name": "Dont have one",
                "phone_number": "Dont need one",
                "close_friend": False,
            },
        ]

        for friend in friends_list:
            models.add_friend(
                friend["first_name"],
                friend["last_name"],
                friend["phone_number"],
                friend["close_friend"],
            )

        self.assertIsNone(models.find_by_name("Gary", "Mod"))
        real_friend = models.find_by_name("Doc", "Louis")
        self.assertIsNotNone(real_friend)
        self.assertEqual(real_friend.close_friend, True)

    # see closest friends only
    def test_view_close_friends(self):
        friends_list = [
            {
                "first_name": "Barack",
                "last_name": "Obama",
                "phone_number": "07-854-839",
                "close_friend": True,
            },
            {
                "first_name": "Doc",
                "last_name": "Louis",
                "phone_number": "014-213-8118",
                "close_friend": True,
            },
            {
                "first_name": "Dog",
                "last_name": "Dont have one",
                "phone_number": "Dont need one",
                "close_friend": False,
            },
        ]

        for friend in friends_list:
            models.add_friend(
                friend["first_name"],
                friend["last_name"],
                friend["phone_number"],
                friend["close_friend"],
            )

        self.assertEqual(len(models.show_close_friends()), 2)

    # change the close friend status of a friend
    def test_change_close_status(self):
        friends_list = [
            {
                "first_name": "Barack",
                "last_name": "Obama",
                "phone_number": "07-854-839",
                "close_friend": True,
            },
            {
                "first_name": "Doc",
                "last_name": "Louis",
                "phone_number": "014-213-8118",
                "close_friend": True,
            },
            {
                "first_name": "Dog",
                "last_name": "Dont have one",
                "phone_number": "Dont need one",
                "close_friend": False,
            },
        ]

        for friend in friends_list:
            models.add_friend(
                friend["first_name"],
                friend["last_name"],
                friend["phone_number"],
                friend["close_friend"],
            )

        models.change_close_status("Dog", True)
        self.assertEqual(models.find_by_name("Dog", "Dont have one").close_friend, True)

    # test remove friend button
    def test_remove_friend(self):
        friends_list = [
            {
                "first_name": "Barack",
                "last_name": "Obama",
                "phone_number": "07-854-839",
                "close_friend": True,
            },
            {
                "first_name": "Doc",
                "last_name": "Louis",
                "phone_number": "014-213-8118",
                "close_friend": True,
            },
            {
                "first_name": "Dog",
                "last_name": "Dont have one",
                "phone_number": "Dont need one",
                "close_friend": False,
            },
        ]

        for friend in friends_list:
            models.add_friend(
                friend["first_name"],
                friend["last_name"],
                friend["phone_number"],
                friend["close_friend"],
            )

        models.remove_friend("Barack")
        self.assertEqual(len(models.show_all()), 2)
