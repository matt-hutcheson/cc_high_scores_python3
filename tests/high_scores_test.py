import unittest

from src.high_scores import latest, personal_best, personal_top_three

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):

    def setUp(self):
        self.scores = [34, 54, 765, 234, 1, 32, 764, 98, 901, 378, 811]

        # Tests

    def test_check_scores_exist(self):
        self.assertEqual(11, len(self.scores))

    # Test latest score (the last thing in the list)



    # Test personal best (the highest score in the list)

    # Test top three from list of scores

    # Test ordered from highest to lowest

    # Test top three when there is a tie

    # Test top three when there are less than three

    # Test top three when there is only one
