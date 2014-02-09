import unittest

import spatial

class SpatialTests(unittest.TestCase):
    def testNN(self):
        hash = spatial.encode(-0.5, -0.5, 1, 1)
        self.assertEqual(spatial.decode(hash, 1, 1), (-0.5, -0.5))

    def testNP(self):
        hash = spatial.encode(-0.5, 0.5, 1, 1)
        self.assertEqual(spatial.decode(hash, 1, 1), (-0.5, 0.5))

    def testPN(self):
        hash = spatial.encode(0.5, -0.5, 1, 1)
        self.assertEqual(spatial.decode(hash, 1, 1), (0.5, -0.5))

    def testPP(self):
        hash = spatial.encode(0.5, 0.5, 1, 1)
        self.assertEqual(spatial.decode(hash, 1, 1), (0.5, 0.5))

    def testLargePP(self):
        hash = spatial.encode(100.7, 20.3, 1, 1)
        self.assertEqual(spatial.decode(hash, 1, 1), (100.5, 20.5))

    def testLargeNP(self):
        hash = spatial.encode(-16.5, 800.1, 1, 1)
        self.assertEqual(spatial.decode(hash, 1, 1), (-16.5, 800.5))

    def testLargePN(self):
        hash = spatial.encode(20.7, -11.4, 1, 1)
        self.assertEqual(spatial.decode(hash, 1, 1), (20.5, -11.5))

    def testLargeNN(self):
        hash = spatial.encode(-2176.8, -11268.1, 1, 1)
        self.assertEqual(spatial.decode(hash, 1, 1), (-2176.5, -11268.5))

    def testLargerGrid(self):
        hash = spatial.encode(-6.8, 202.3, 10, 10)
        self.assertEqual(spatial.decode(hash, 10, 10), (-5, 205))

    def testUnevenGrid(self):
        hash = spatial.encode(-6.8, 211.3, 10, 50)
        self.assertEqual(spatial.decode(hash, 10, 50), (-5, 225))

