from django.test import TestCase

from inventory.models import Laptop, Mobile


class LaptopsListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Laptop.objects.create(
            type="MACBOOK",
            status="AVAILABLE",
        )

    def test_display_laptops_view_url_exists_at_desired_location(self):
        response = self.client.get('/display_laptops')
        self.assertEqual(response.status_code, 200)

    def test_add_laptops_view_url_exists_at_desired_location(self):
        response = self.client.get('/add_laptop')
        self.assertEqual(response.status_code, 200)

    def test_edit_laptops_view_url_exists_at_desired_location(self):
        response = self.client.get('/edit_laptop/1')
        self.assertEqual(response.status_code, 200)

    def test_laptops_view_uses_correct_template(self):
        response = self.client.get('/display_laptops')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inventory/index.html')

    def test_add_laptops_view_uses_correct_template(self):
        response = self.client.get('/add_laptop')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inventory/add_new.html')

    def test_edit_laptops_view_uses_correct_template(self):
        response = self.client.get('/edit_laptop/1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inventory/edit_item.html')


class MobilesListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Mobile.objects.create(
            type="IPHONE",
            status="AVAILABLE",
        )

    def test_display_mobiles_view_url_exists_at_desired_location(self):
        response = self.client.get('/display_mobiles')
        self.assertEqual(response.status_code, 200)

    def test_add_mobiles_view_url_exists_at_desired_location(self):
        response = self.client.get('/add_mobile')
        self.assertEqual(response.status_code, 200)

    def test_edit_mobiles_view_url_exists_at_desired_location(self):
        response = self.client.get('/edit_mobile/1')
        self.assertEqual(response.status_code, 200)

    def test_mobiles_view_uses_correct_template(self):
        response = self.client.get('/display_mobiles')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inventory/index.html')

    def test_add_mobiles_view_uses_correct_template(self):
        response = self.client.get('/add_mobile')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inventory/add_new.html')

    def test_edit_mobiles_view_uses_correct_template(self):
        response = self.client.get('/edit_mobile/1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inventory/edit_item.html')
