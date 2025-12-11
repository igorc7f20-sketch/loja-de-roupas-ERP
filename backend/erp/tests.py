from django.test import TestCase

class SmokeTest(TestCase):
    def test_soma_simples(self):
        assert 1 + 1 == 2