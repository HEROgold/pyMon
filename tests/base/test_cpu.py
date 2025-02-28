import unittest
from pymon.base.cpu import CPUMeter, CPUStats

class TestCPUStats(unittest.TestCase):
    def setUp(self):
        self.stats = CPUStats()

    def test_validate(self):
        self.assertTrue(self.stats.validate())

class TestCPUMeter(unittest.TestCase):
    def setUp(self):
        self.meter = CPUMeter()

    def test_validate(self):
        with self.assertRaises(NotImplementedError):
            self.meter.validate()

    def test_render(self):
        with self.assertRaises(NotImplementedError):
            self.meter.render()

if __name__ == "__main__":
    unittest.main()
