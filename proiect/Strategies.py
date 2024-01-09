import random


def easy_strategy(game):
    available = False
    while not available:
        random_column = random.randint(0, game.board.columns - 1)
        if game.board.add_disc(game.player2, random_column):
            available = True


def medium_strategy(game):
    for col in range(game.board.columns):
        if game.board.is_valid_move(col):
            game.board.add_disc(game.current_player, col)
            if game.board.found_4_in_a_row(game.current_player.color):
                return
            game.board.remove_disc(col)

    opponent = game.get_opponent()
    for col in range(game.board.columns):
        if game.board.is_valid_move(col):
            game.board.add_disc(opponent, col)
            if game.board.found_4_in_a_row(opponent.color):
                game.board.remove_disc(col)
                game.board.add_disc(game.current_player, col)
                return
            game.board.remove_disc(col)

    strategic_move = find_strategic_move_medium(game)
    if strategic_move is not None:
        game.board.add_disc(game.current_player, strategic_move)
        return

    easy_strategy(game)


def find_strategic_move_medium(game):
    center_column = game.board.columns // 2
    if game.board.is_valid_move(center_column):
        return center_column

    for col in range(game.board.columns):
        if game.board.is_valid_move(col):
            return col

    return None


def hard_strategy(game):
    for col in range(game.board.columns):
        if game.board.is_valid_move(col):
            game.board.add_disc(game.current_player, col)
            if game.board.found_4_in_a_row(game.current_player.color):
                return
            game.board.remove_disc(col)

    opponent = game.get_opponent()
    for col in range(game.board.columns):
        if game.board.is_valid_move(col):
            game.board.add_disc(opponent, col)
            if game.board.found_4_in_a_row(opponent.color):
                game.board.remove_disc(col)
                game.board.add_disc(game.current_player, col)
                return
            game.board.remove_disc(col)

    strategic_move = find_strategic_move_hard(game)
    if strategic_move is not None:
        game.board.add_disc(game.current_player, strategic_move)
        return

    easy_strategy(game)


def find_strategic_move_hard(game):
    center_column = game.board.columns // 2
    if game.board.is_valid_move(center_column):
        return center_column

    for col in range(game.board.columns):
        if game.board.is_valid_move(col):
            game.board.add_disc(game.current_player, col)
            if can_create_two_in_a_row(game):
                game.board.remove_disc(col)
                return col
            game.board.remove_disc(col)

    return None


def can_create_two_in_a_row(game):
    for col in range(game.board.columns):
        if game.board.is_valid_move(col):
            game.board.add_disc(game.current_player, col)
            if game.board.found_4_in_a_row(game.current_player.color):
                game.board.remove_disc(col)
                return True
            game.board.remove_disc(col)
    return False
