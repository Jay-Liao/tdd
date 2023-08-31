import unittest


class Tennis(object):
    def __init__(self):
        self.left_score = 0
        self.right_score = 0

    def left_increase_score(self):
        self.left_score += 1

    def right_increase_score(self):
        self.right_score += 1
        return self.display()

    def display(self):
        return "love all"


class TennisTest(unittest.TestCase):
    def test_something(self):
        tennis = Tennis()
        # 0:0
        self.assertEqual("love all", tennis.display())
        # 0:1


if __name__ == '__main__':
    unittest.main()
