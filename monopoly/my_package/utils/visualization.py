from ..data_structs.game_board import GameBoard
import matplotlib.pyplot as plt

class VisualizationsResultRols:
    def __init__(
            self,
            figsize:tuple=(12, 9),
            title_figure:str=None,
            grid_visible:bool=False
    ):
        self._figsize = figsize
        self._title_figure = title_figure
        self._grid_visible = grid_visible

    def create_hist(self, game_board:GameBoard):
        fig, ax = plt.subplots(figsize=self._figsize)
        ax.bar(game_board.names_place, game_board.places.values())
        ax.set_xticklabels(game_board.names_place, rotation=45, ha='right')
        self._init_parametres(ax)

        return fig

    def _init_parametres(self, ax):
        ax.grid(visible=self._grid_visible)
        ax.set_title(self._title_figure)
        ax.legend()