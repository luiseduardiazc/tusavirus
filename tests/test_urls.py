import unittest
from django.test import Client


class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_get_calculate(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_root_resolved(self):
        response = self.client.get('/?get_report=&get_data=Calculate')

        self.assertEqual(response.status_code, 200)
