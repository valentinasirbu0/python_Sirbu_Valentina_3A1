import random


def easy_strategy(game):
    available = False
    while not available:
        random_column = random.randint(0, game.board.columns - 1)
        if game.board.add_disc(game.player2, random_column):
            available = True


def medium_strategy(game):
    # Check for a winning move
    for col in range(game.board.columns):
        if game.board.is_valid_move(col):
            game.board.add_disc(game.current_player, col)
            if game.board.found_4_in_a_row(game.current_player.color):
                return
            game.board.remove_disc(col)

    # Check for a blocking move against the opponent
    opponent = game.get_opponent()
    for col in range(game.board.columns):
        if game.board.is_valid_move(col):
            game.board.add_disc(opponent, col)
            if game.board.found_4_in_a_row(opponent.color):
                game.board.remove_disc(col)
                game.board.add_disc(game.current_player, col)
                return
            game.board.remove_disc(col)

    # If no winning or blocking move, make a strategic move
    strategic_move = find_strategic_move_medium(game)
    if strategic_move is not None:
        game.board.add_disc(game.current_player, strategic_move)
        return

    # If no strategic move, fallback to an easy strategy
    easy_strategy(game)


def find_strategic_move_medium(game):
    # Add your own logic to find a strategic move
    # For example, you might prioritize the center column
    center_column = game.board.columns // 2
    if game.board.is_valid_move(center_column):
        return center_column

    # If the center is not available, find the first available column
    for col in range(game.board.columns):
        if game.board.is_valid_move(col):
            return col

    # No available moves
    return None


def hard_strategy(game):
    # Check for a winning move
    for col in range(game.board.columns):
        if game.board.is_valid_move(col):
            game.board.add_disc(game.current_player, col)
            if game.board.found_4_in_a_row(game.current_player.color):
                return
            game.board.remove_disc(col)

    # Check for a blocking move against the opponent
    opponent = game.get_opponent()
    for col in range(game.board.columns):
        if game.board.is_valid_move(col):
            game.board.add_disc(opponent, col)
            if game.board.found_4_in_a_row(opponent.color):
                game.board.remove_disc(col)
                game.board.add_disc(game.current_player, col)
                return
            game.board.remove_disc(col)

    # If no winning or blocking move, make a strategic move
    strategic_move = find_strategic_move_hard(game)
    if strategic_move is not None:
        game.board.add_disc(game.current_player, strategic_move)
        return

    # If no strategic move, fallback to an easy strategy
    easy_strategy(game)


def find_strategic_move_hard(game):
    # Prioritize the center column if available
    center_column = game.board.columns // 2
    if game.board.is_valid_move(center_column):
        return center_column

    # Check for an opportunity to create two in a row and block the opponent
    for col in range(game.board.columns):
        if game.board.is_valid_move(col):
            game.board.add_disc(game.current_player, col)
            if can_create_two_in_a_row(game):
                game.board.remove_disc(col)
                return col
            game.board.remove_disc(col)

    # If no strategic move is found, return None
    return None


def can_create_two_in_a_row(game):
    # Check if the current player has a chance to create two in a row
    for col in range(game.board.columns):
        if game.board.is_valid_move(col):
            game.board.add_disc(game.current_player, col)
            if game.board.found_4_in_a_row(game.current_player.color):
                game.board.remove_disc(col)
                return True
            game.board.remove_disc(col)
    return False
