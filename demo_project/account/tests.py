from rest_framework.test import APITestCase
from django.urls import reverse


class UserTest(APITestCase):
    def setUp(self):
        self.index_url = reverse('index')
        self.register_url = reverse('create')

        self.user_data = {
            "first_name": "qwer",
            "last_name": "qwwerty",
            "email": "s1@gmail.com",
            "password": "sudhagar",
            "address": "{'local': 'chennai'}",
            "qualification": "{'ug': 'Btech'}"
        }

        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()


class UserTestView(UserTest):
    def test_index(self):
        res = self.client.get(self.index_url)
        self.assertEqual(res.status_code, 200)

    def test_user_can_register_with_data(self):
        res = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(res.status_code, 201)

    def test_user_can_register_with_no_data(self):
        res = self.client.post(self.register_url, format='json')
        self.assertEqual(res.status_code, 400)


