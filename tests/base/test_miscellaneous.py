import unittest
from pymon.base.miscellaneous import MiscellaneousMeter, MiscellaneousStats

class TestMiscellaneousStats(unittest.TestCase):
    def setUp(self):
        self.stats = MiscellaneousStats()

    def test_validate(self):
        with self.assertRaises(NotImplementedError):
            self.stats.validate()

class TestMiscellaneousMeter(unittest.TestCase):
    def setUp(self):
        self.meter = MiscellaneousMeter()

    def test_validate(self):
        with self.assertRaises(NotImplementedError):
            self.meter.validate()

    def test_render(self):
        with self.assertRaises(NotImplementedError):
            self.meter.render()

if __name__ == "__main__":
    unittest.main()
