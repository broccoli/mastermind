'''
Created on Jun 8, 2015

@author: richard
'''

from mastermind import Game

NUM_TURNS = 10
NUM_PEGS = 4



if __name__ == '__main__':
    game = Game(show_code = True)
    game.play_game()
