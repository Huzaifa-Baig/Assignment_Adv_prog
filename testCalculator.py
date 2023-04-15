import unittest


class TestGasPrice(unittest.TestCase):

    def test_gas_price(self):
        gal = 10
        litre = gal * 5.9
        bar = gal / 9.5
        petrol = gal * 25.7
        price = gal * 6.8

        self.assertAlmostEqual(litre, 59.0, delta=0.01)
        self.assertAlmostEqual(bar, 1.05263157895, delta=0.01)
        self.assertAlmostEqual(petrol, 257.0, delta=0.01)
        self.assertAlmostEqual(price, 68.0, delta=0.01)


if __name__ == '__main__':
    unittest.main()









