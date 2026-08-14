import unittest

from my_package.game.course_game import GameCubes

class TestRollOfDice(unittest.TestCase):
    def setUp(self):
        distribution_two_cubics = [
            0.02,
            0.05,
            0.08,
            0.12,
            0.18,
            0.30,
            0.12,
            0.06,
            0.04,
            0.02,
            0.01
        ]
        self.cubes = GameCubes(distribution_two_cubics)
        
    def test_check_range_distribution(self):
        count_iter = 10000

        for _ in range(count_iter):
            sum_roll = self.cubes.roll_of_dice()

            self.assertTrue(2 <= sum_roll <= 12, 'Сумма должна быть от 2 до 12, включая границы!')

if __name__ == '__main__':
    unittest.main()