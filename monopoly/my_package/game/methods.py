from ..data_structs.game_board import GameBoard
from . import GameCubes

def walk(number_start_place:int, count_iter:int, logic_cubes:GameCubes) -> GameBoard:
    board = GameBoard()

    for _ in range(count_iter):
        now_roll = logic_cubes.roll_of_dice()
        result_number_place = number_start_place + now_roll
        board[result_number_place] += 1
        number_start_place = result_number_place

    return board

    