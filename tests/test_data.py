from unittest import TestCase
from utils.utils import dataSource

class SampleUnittest(TestCase):

    def checkDataEqual(self):
        testData = {
            "one": 1,
            "two": 2,
            "three": 3,
        }
        data = dataSource()
        self.assertEqual(data, testData)

