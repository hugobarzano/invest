from django.test import TestCase

class SystemTestCase(TestCase):

    def test_system(self):
        print("Invest project testing\n")
        self.assertEqual(True, True)