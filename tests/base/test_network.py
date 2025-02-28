import unittest
from pymon.base.network import NetworkMeter, NetworkStats

class TestNetworkStats(unittest.TestCase):
    def setUp(self):
        self.stats = NetworkStats()

    def test_validate(self):
        with self.assertRaises(NotImplementedError):
            self.stats.validate()

class TestNetworkMeter(unittest.TestCase):
    def setUp(self):
        self.meter = NetworkMeter()

    def test_validate(self):
        with self.assertRaises(NotImplementedError):
            self.meter.validate()

    def test_render(self):
        with self.assertRaises(NotImplementedError):
            self.meter.render()

if __name__ == "__main__":
    unittest.main()
