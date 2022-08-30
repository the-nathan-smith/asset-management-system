from django.test import TestCase

from inventory.forms import LaptopForm, MobileForm

class LaptopFormTest(TestCase):
    def testLaptopFormTypeLabel(self):
        form = LaptopForm()
        self.assertEqual(form.fields['type'].label, "Type")

    def testLaptopFormOwnerLabel(self):
        form = LaptopForm()
        self.assertEqual(form.fields['owner'].label, "Owner")

    def testLaptopFormStatusLabel(self):
        form = LaptopForm()
        self.assertEqual(form.fields['status'].label, "Status")


class MobileFormTest(TestCase):
    def testMobileFormTypeLabel(self):
        form = MobileForm()
        self.assertEqual(form.fields['type'].label, "Type")

    def testMobileFormOwnerLabel(self):
        form = MobileForm()
        self.assertEqual(form.fields['owner'].label, "Owner")

    def testMobileFormStatusLabel(self):
        form = MobileForm()
        self.assertEqual(form.fields['status'].label, "Status")
