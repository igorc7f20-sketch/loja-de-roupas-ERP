from django.test import TestCase

class SmokeTest(TestCase):
    def test_math_works(self):
        """Um teste simples para garantir que o pytest roda"""
        self.assertEqual(1 + 1, 2)
        