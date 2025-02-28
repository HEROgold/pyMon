import unittest
from pymon.base.disk import DiskMeter, DiskStats

class TestDiskStats(unittest.TestCase):
    def setUp(self):
        self.stats = DiskStats()

    def test_validate(self):
        with self.assertRaises(NotImplementedError):
            self.stats.validate()

class TestDiskMeter(unittest.TestCase):
    def setUp(self):
        self.meter = DiskMeter()

    def test_validate(self):
        with self.assertRaises(NotImplementedError):
            self.meter.validate()

    def test_render(self):
        with self.assertRaises(NotImplementedError):
            self.meter.render()

if __name__ == "__main__":
    unittest.main()
