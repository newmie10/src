import random
import numpy as np

class BackgammonGame:
    def __init__(self):
        # input positive values for player 1, nagative for player 2
        self.board = [0] * 24

        self.player_home = [0, 0]