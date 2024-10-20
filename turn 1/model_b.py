import unittest
import pandas as pd


class TestDataProfiling(unittest.TestCase):

    def test_profile_column_accuracy(self):
        # Test case 1: Checking accuracy for a normal distribution
        data = pd.DataFrame({'col1': [1, 2, 3, 4, 5]})
        expected_profile = {'mean': 3.0, 'median': 3.0, 'std': 1.4142135623730951}
        actual_profile = profile_column(data['col1'])
        self.assertAlmostEqual(actual_profile['mean'], expected_profile['mean'], places=6)
        self.assertAlmostEqual(actual_profile['median'], expected_profile['median'], places=6)
        self.assertAlmostEqual(actual_profile['std'], expected_profile['std'], places=6)

        # Test case 2: Checking accuracy for a skewed distribution
        data = pd.DataFrame({'col1': [1, 2, 3, 100, 200]})
        expected_profile = {'mean': 53.2, 'median': 3.0, 'std': 78.02882743344808}
        actual_profile = profile_column(data['col1'])
        self.assertAlmostEqual(actual_profile['mean'], expected_profile['mean'], places=6)
        self.assertAlmostEqual(actual_profile['median'], expected_profile['median'], places=6)
        self.assertAlmostEqual(actual_profile['std'], expected_profile['std'], places=6)


if __name__ == '__main__':
    unittest.main()
