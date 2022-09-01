from django.test import TestCase

from inventory.models import Laptop, Mobile


class LaptopModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Laptop.objects.create(type="MACBOOK", status="AVAILABLE")

    def setUp(self):
        pass

    def test_type_max_length(self):
        laptop = Laptop.objects.get(id=1)
        max_length = laptop._meta.get_field('type').max_length
        self.assertEqual(max_length, 100)

    def test_status_max_length(self):
        laptop = Laptop.objects.get(id=1)
        max_length = laptop._meta.get_field('status').max_length
        self.assertEqual(max_length, 100)

    def test_laptop_string_is_correctly_formatted(self):
        laptop = Laptop.objects.get(id=1)
        expected_string = f'Type: {laptop.type} | Owner: {laptop.owner} | Status: {laptop.status}'
        self.assertEqual(str(laptop), expected_string)


class MobileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Mobile.objects.create(type="IPHONE", status="AVAILABLE")

    def setUp(self):
        pass

    def test_type_max_length(self):
        mobile = Mobile.objects.get(id=1)
        max_length = mobile._meta.get_field('type').max_length
        self.assertEqual(max_length, 100)

    def test_status_max_length(self):
        mobile = Mobile.objects.get(id=1)
        max_length = mobile._meta.get_field('status').max_length
        self.assertEqual(max_length, 100)

    def test_mobile_string_is_correctly_formatted(self):
        mobile = Mobile.objects.get(id=1)
        expected_string = f'Type: {mobile.type} | Owner: {mobile.owner} | Status: {mobile.status}'
        self.assertEqual(str(mobile), expected_string)
