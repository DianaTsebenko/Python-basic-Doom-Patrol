import unittest
import functions_for_testing as fft


class FunctionsTest(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(fft.suma(4, 5), 9)
        self.assertNotEqual(fft.suma(3, 4), 6)
        self.assertEqual(fft.suma(100, 150), 250)

    def test_dif(self):
        self.assertEqual(fft.dif(5, 1), 4)
        self.assertNotEqual(fft.dif(3, 4), 1)
        self.assertEqual(fft.dif(140, 149), -9)

    def test_div(self):
        try:
            fft.div(15, 0)
        except ZeroDivisionError:
            self.assertEqual(0, 0)
        self.assertEqual(fft.div(5, 2), 2.5)
        self.assertNotEqual(fft.div(6, 4), 64)
        self.assertEqual(fft.div(200, 100), 2)

    def test_multiple(self):
        self.assertEqual(fft.multiple(5, 2), 10)
        self.assertNotEqual(fft.multiple(6, 4), 11)
        self.assertEqual(fft.multiple(200, 100), 20000)