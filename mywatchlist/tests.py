from django.test import TestCase, Client
from django.urls import reverse

class StatusTest(TestCase):
    def test_show_mywatchlist_html(self):
        client = Client() 
        response = client.get(reverse('mywatchlist:show_mywatchlist_html'))

        self.assertEqual(response.status_code, 200)

