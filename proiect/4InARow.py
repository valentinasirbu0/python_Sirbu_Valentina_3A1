import sys

from Classes import Player, Game
import Interface


def initialize_game(role2, rows, columns, first_player="human"):
    player1 = Player((255, 0, 127), "human")
    player2 = Player((0, 255, 128), role2)
    if first_player == "human":
        game = Game(rows, columns, player1, player1, player2)
    else:
        game = Game(rows, columns, player2, player1, player2)
    return game


'''
def make_a_move(game):
    if game.current_player.role == "ai":
        if game.level == "easy":
            Strategies.easy_strategy(game)
        elif game.level == "medium":
            Strategies.medium_strategy(game)
        elif game.level == "hard":
            Strategies.hard_strategy(game)
    else:
        our_input = input("Enter something: ")
        game.board.add_disc(game.current_player, int(our_input))


def play_game(game):
    while game.winner is None:
        if game.no_more_moves():
            print("No more moves available")
            break
        else:
            make_a_move(game)
            game.change_current_player()
            game.board.print_board()
            if game.winner_found():
                print("Congratulations to ", game.winner.color)
                break
'''

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Insuficient parameters")
    else:
        if len(sys.argv) >= 5 and sys.argv[4] is not None:
            game = initialize_game(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4])
        else:
            game = initialize_game(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
    Interface.FourInARowWindow(game)