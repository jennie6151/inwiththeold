from django.test import TestCase
from .models import Antique

class TestViews(TestCase):
    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")

    def test_get_antique_list_page(self):
        page = self.client.get("/antiques")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "antique_list.html")

    def test_get_antique_detail_page(self):
        item = Antique(name='Create a test')
        item.save()

        page = self.client.get("/antique/{0}".format(antique.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "antique_detail.html")