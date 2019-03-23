# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
def fun(x):
    return x + 1

class MyTest(TestCase):

    def test_dummy(self):
        self.assertEqual(fun(3), 4)





