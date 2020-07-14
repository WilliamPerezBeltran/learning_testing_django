from django.test import TestCase
from test1.models import Contact
import pdb


class TestStudentContactForm(TestCase):
    def test_can_send_message(self):
        data = {
            "first_name": "Juliana",
            "last_name": " Crain",
            "message": "Would love to talk about Philip K. Dick",
        }
        response = self.client.post("/contact/", data=data)
        self.assertEqual(Contact.objects.count(), 1)
