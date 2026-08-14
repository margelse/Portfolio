from ..data_structs.game_board import GameBoard
from ..game.course_game import GameCubes

import unittest

from ..game import walk

class TestWalk(unittest.TestCase):
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
        self.logic_cubes = GameCubes(distribution_two_cubics)

    def test_sum_count_roll(self):
        result_board = walk(0, 100, self.logic_cubes)
        sum_count_roll = sum(list(result_board.places.values()))

        self.assertEqual(sum_count_roll, 100, f'Неверная сумма бросков. {result_board}')
        print(result_board)