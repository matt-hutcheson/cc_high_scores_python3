import unittest

from src.high_scores import *

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):

    def setUp(self):
        self.scores = [34, 54, 765, 234, 1, 32, 764, 98, 901, 378, 811]

        # Tests

    def test_check_scores_exist(self):
        self.assertEqual(11, len(self.scores))

    # Test latest score (the last thing in the list)

    def test_latest_score(self):
        self.assertEqual(811, latest(self.scores))

    # Test personal best (the highest score in the list)

    def test_get_personal_best(self):
        self.assertEqual(901, personal_best(self.scores))

    # Test top three from list of scores

    def test_get_top_three(self):
        self.assertEqual([901, 811, 765], personal_top_three(self.scores))

    # Test ordered from highest to lowest
    def test_list_is_ordered_highest_to_lowest(self):
        self.assertEqual([901, 811, 765, 764, 378, 234, 98, 54, 34, 32, 1], get_sorted_list(self.scores))

    # Test top three when there is a tie

    # Test top three when there are less than three

    # Test top three when there is only one
