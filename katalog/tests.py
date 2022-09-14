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
        kura_kura_mainan = CatalogItem.objects.get( item_name = 'kura-kura mainan', 
                                                    item_price = 5, 
                                                    item_stock = 3,
                                                    description = 'bukan kura-kura hidup', 
                                                    rating = 10000, 
                                                    item_url = 'http://tokopedia.com/tokotokoan/kura-kura-mainan')

        kura_kura_betulan = CatalogItem.objects.get(item_name = 'kura-kura betulan',
                                                    item_price = 50000, 
                                                    item_stock = 1,
                                                    description = 'kura-kura hidup', 
                                                    rating = 10000, 
                                                    item_url = 'http://tokopedia.com/tokotokoan/kura-kura-betulan')
        
        self.assertEqual(kura_kura_mainan.item_name, 'kura-kura mainan')
        self.assertEqual(kura_kura_mainan.item_price, 5)
        self.assertEqual(kura_kura_mainan.item_stock, 3)
        self.assertEqual(kura_kura_mainan.description, 'bukan kura-kura hidup')
        self.assertEqual(kura_kura_mainan.rating, 10000)
        self.assertEqual(kura_kura_mainan.item_url, 'http://tokopedia.com/tokotokoan/kura-kura-mainan')

        self.assertEqual(kura_kura_betulan.item_name, 'kura-kura betulan')
        self.assertEqual(kura_kura_betulan.item_price, 50000)
        self.assertEqual(kura_kura_betulan.item_stock, 1)
        self.assertEqual(kura_kura_betulan.description, 'kura-kura hidup')
        self.assertEqual(kura_kura_betulan.rating, 10000)
        self.assertEqual(kura_kura_betulan.item_url, 'http://tokopedia.com/tokotokoan/kura-kura-betulan')

