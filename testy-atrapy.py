from unittest import mock

class TestWithMocks(unittest.TestCase):
    
    @mock.patch('random.randint')
    def test_get_random_prime_prime_number(self, mock_randint):
        mock_randint.return_value = 7
        result = get_random_prime()
        self.assertEqual(result, 7)
    
    @mock.patch('random.randint')
    def test_get_random_prime_not_prime_number(self, mock_randint):
        mock_randint.return_value = 10
        result = get_random_prime()
        self.assertIsNone(result)

    @mock.patch('random.choice')
    def test_external_data_fetch_prime(self, mock_choice):
        mock_choice.return_value = 29
        result = get_prime_from_external_data()
        self.assertTrue(result)

    @mock.patch('random.choice')
    def test_external_data_fetch_not_prime(self, mock_choice):
        mock_choice.return_value = 30
        result = get_prime_from_external_data()
        self.assertFalse(result)

    @mock.patch('random.choice')
    @mock.patch('random.randint')
    def test_combined_mock(self, mock_randint, mock_choice):
        mock_randint.return_value = 11
        mock_choice.return_value = 29
        self.assertEqual(get_random_prime(), 11)
        self.assertTrue(get_prime_from_external_data())
