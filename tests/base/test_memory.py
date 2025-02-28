import unittest
from pymon.base.memory import MemoryMeter, MemoryStats

class TestMemoryStats(unittest.TestCase):
    def setUp(self):
        self.stats = MemoryStats()

    def test_validate(self):
        with self.assertRaises(NotImplementedError):
            self.stats.validate()

class TestMemoryMeter(unittest.TestCase):
    def setUp(self):
        self.meter = MemoryMeter()

    def test_validate(self):
        with self.assertRaises(NotImplementedError):
            self.meter.validate()

    def test_render(self):
        with self.assertRaises(NotImplementedError):
            self.meter.render()

if __name__ == "__main__":
    unittest.main()
