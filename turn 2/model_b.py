import unittest


def profile_missing_values(data, missing_values=None):
    if missing_values is None:
        missing_values = [None]

    missing_count = sum(value in missing_values for value in data)
    total_count = len(data)
    if total_count == 0:
        return 0.0
    return missing_count / total_count


class TestDataProfiling(unittest.TestCase):

    def test_profile_missing_values_correctly_identifies_missing_data(self):
        test_data = [1, 2, None, 4, None, 5]
        expected_missing_rate = 2 / 6
        self.assertAlmostEqual(profile_missing_values(test_data), expected_missing_rate, places=2)

    def test_profile_missing_values_handles_empty_data(self):
        test_data = []
        expected_missing_rate = 0.0
        self.assertEqual(profile_missing_values(test_data), expected_missing_rate)

    def test_profile_missing_values_handles_no_missing_data(self):
        test_data = [1, 2, 3, 4, 5]
        expected_missing_rate = 0.0
        self.assertEqual(profile_missing_values(test_data), expected_missing_rate)

    def test_profile_missing_values_handles_empty_strings_as_missing(self):
        test_data = [1, 2, '', 4, '', 5]
        expected_missing_rate = 2 / 6
        self.assertAlmostEqual(profile_missing_values(test_data, missing_values=['']), expected_missing_rate, places=2)

    def test_profile_missing_values_handles_custom_missing_values(self):
        test_data = [1, 2, 'NA', 4, 'NA', 5]
        expected_missing_rate = 2 / 6
        self.assertAlmostEqual(profile_missing_values(test_data, missing_values=['NA']), expected_missing_rate,
                               places=2)

    def test_profile_missing_values_ignores_specify_missing_values_when_not_given(self):
        test_data = [1, 2, 'NA', 4, 'NA', 5]
        expected_missing_rate = 0.0  # Default behavior doesn't consider 'NA' as missing
        self.assertAlmostEqual(profile_missing_values(test_data), expected_missing_rate, places=2)


if __name__ == '__main__':
    unittest.main() 
