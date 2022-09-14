from django.test import TestCase
from katalog.models import CatalogItem

# Create your tests here.
class KatalogTestCase(TestCase):
    def setUp(self):
        CatalogItem.objects.create( item_name = 'kura-kura mainan', 
                                    item_price = 5, item_stock = 3,
                                    description = 'bukan kura-kura hidup', rating = 10000, 
                                    item_url = 'http://tokopedia.com/tokotokoan/kura-kura-mainan');

        CatalogItem.objects.create( item_name = 'kura-kura betulan',
                                    item_price = 50000, 
                                    item_stock = 1,
                                    description = 'kura-kura hidup', 
                                    rating = 10000, 
                                    item_url = 'http://tokopedia.com/tokotokoan/kura-kura-betulan');
                                
    def test_katalog_is_correct(self):
        kura_kura_mainan = CatalogItem.objects.get(item_name = 'kura-kura mainan')
        kura_kura_betulan = CatalogItem.objects.get(item_name = 'kura-kura betulan')

        self.assertEqual()

        self.assertEqual()