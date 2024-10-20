import unittest

def profile_missing_values(data):
	missing_count = sum(1 for value in data if value is None)
	total_count = len(data)
	if total_count == 0:
		return 0.0
	return missing_count / total_count

class TestDataProfiling(unittest.TestCase):

	def test_profile_missing_values_correctly_identifies_missing_data(self):
		test_data = [1, 2, None, 4, None, 5]
		expected_missing_rate = 2/6
		self.assertAlmostEqual(profile_missing_values(test_data), expected_missing_rate, places=2)

	def test_profile_missing_values_handles_empty_data(self):
		test_data = []
		expected_missing_rate = 0.0
		self.assertEqual(profile_missing_values(test_data), expected_missing_rate)

	def test_profile_missing_values_handles_no_missing_data(self):
		test_data = [1, 2, 3, 4, 5]
		expected_missing_rate = 0.0
		self.assertEqual(profile_missing_values(test_data), expected_missing_rate)

if __name__ == '__main__':
	unittest.main()
