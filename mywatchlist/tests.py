from django.test import TestCase

class StatusTest(TestCase):
    def test_show_mywatchlist_html(self):
        response = self.client.get("/html")
        self.assertEqual(response.status_code, 200)

