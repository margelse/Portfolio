import unittest

from ..data_structs.game_board import GameBoard

class TestGameBoard(unittest.TestCase):
    def setUp(self):
        self.board = GameBoard()

    def test_go_borders_out(self):
        number_place_0 = 2
        number_place_1 = 40
        number_place_2 = 79
        number_place_3 = 90

        self.board[number_place_0] += 1
        self.board[number_place_1] += 1
        self.board[number_place_2] += 1
        self.board[number_place_3] += 1

        self.assertEqual(self.board[2], 1, f'Ошибка добавления элемента после завершения первого круга. {self.board.places}')
        self.assertEqual(self.board[0], 1, f'Ошибка добавления элемента после завершения первого круга. {self.board.places}')
        self.assertEqual(self.board[39], 1, f'Ошибка добавления элемента в конце второго круга. {self.board.places}')
        self.assertEqual(self.board[10], 1, f'Ошибка добавления элемента после в 3 круге. {self.board.places}')

if __name__ == '__main__':
    unittest.main()