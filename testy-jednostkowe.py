import unittest

class TestIsPrime(unittest.TestCase):
    
    def test_prime_2(self):
        self.assertTrue(is_prime(2))

    def test_prime_3(self):
        self.assertTrue(is_prime(3))

    def test_not_prime_1(self):
        self.assertFalse(is_prime(1))
    
    def test_not_prime_0(self):
        self.assertFalse(is_prime(0))

    def test_not_prime_negative(self):
        self.assertFalse(is_prime(-5))

    def test_not_prime_even_number(self):
        self.assertFalse(is_prime(4))

    def test_large_prime(self):
        self.assertTrue(is_prime(29))

    def test_large_not_prime(self):
        self.assertFalse(is_prime(100))

    def test_prime_boundary_case(self):
        self.assertTrue(is_prime(17))

    def test_not_prime_boundary_case(self):
        self.assertFalse(is_prime(25))


if __name__ == '__main__':
    unittest.main()