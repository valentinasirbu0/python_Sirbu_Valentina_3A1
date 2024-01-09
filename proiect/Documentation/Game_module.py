"""
Game Module
===============

This module provides a function to initialize a game of 4InARow.

"""

import sys
import pygame
import random


class Game:
    def __init__(self, rows, columns, current_player, player1, player2):
        '''
        Inițializează un joc nou.

        Args:
            rows (int): Numărul de rânduri ale tablei de joc.
            columns (int): Numărul de coloane ale tablei de joc.
            current_player (Player): Jucătorul curent care își va începe mutarea.
            player1 (Player): Jucătorul 1 cu atribute precum culoare și rol.
            player2 (Player): Jucătorul 2 cu atribute precum culoare și rol.
        '''
        self.board = Board(rows, columns)
        self.current_player = current_player
        self.player1 = player1
        self.player2 = player2
        self.winner = None
        self.level = None

    def reset(self):
        '''
        Resetează starea jocului la cea inițială.
        '''
        self.board.reset()
        self.current_player = self.player1
        self.winner = None
        self.level = None

    def set_level(self, level):
        '''
        Setează nivelul de dificultate al jocului.

        Args:
            level (str): Nivelul de dificultate ales: "easy", "medium", sau "hard".
        '''
        self.level = level

    def no_more_moves(self):
        '''
        Verifică dacă nu mai există mutări valide disponibile pe tablă.

        Returns:
            bool: True dacă nu mai există mutări, False altfel.
        '''
        for row in range(self.board.rows - 1):
            for col in range(self.board.columns - 1):
                if self.board.matrix[row][col] == (224, 224, 224):
                    return False
        return True

    def change_current_player(self):
        '''
        Schimbă jucătorul curent cu celălalt jucător.
        '''
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def get_opponent(self):
        '''
        Returnează adversarul jucătorului curent.

        Returns:
            Player: Jucătorul adversar.
        '''
        if self.current_player == self.player1:
            return self.player2
        else:
            return self.player1

    def winner_found(self):
        '''
        Verifică dacă s-a îndeplinit o condiție de câștig și actualizează câștigătorul.

        Returns:
            bool: True dacă există un câștigător, False altfel.
        '''
        if self.board.found_4_in_a_row(self.player1.color):
            self.winner = self.player1
            return True
        elif self.board.found_4_in_a_row(self.player2.color):
            self.winner = self.player2
            return True
        return False


class Player:
    def __init__(self, color, role):
        '''
        Inițializează un obiect Player cu o culoare specifică și un rol.

        Args:
            color (tuple): Tripletă RGB reprezentând culoarea jucătorului.
            role (str): Rolul jucătorului, cum ar fi "human" sau "ai".
        '''
        self.color = color
        self.role = role


class Board:
    def __init__(self, rows, columns):
        '''
        Inițializează tabla de joc cu un număr specific de rânduri și coloane.

        Args:
            rows (int): Numărul de rânduri ale tablei de joc.
            columns (int): Numărul de coloane ale tablei de joc.
        '''
        self.rows = rows
        self.columns = columns
        self.matrix = [[(224, 224, 224) for _ in range(columns)] for _ in range(rows)]

    def __getitem__(self, index):
        '''
        Returnează rândul specificat din matricea tablei de joc.

        Args:
            index (int): Indexul rândului.

        Returns:
            list: Rândul specificat din matricea tablei de joc.
        '''
        return self.matrix[index]

    def reset(self):
        '''
        Resetează tabla de joc, umplând-o cu culoarea inițială specificată.
        '''
        self.matrix = [[(224, 224, 224) for _ in range(self.columns)] for _ in range(self.rows)]

    def print_board(self):
        '''
        Afișează conținutul tablei de joc, util în scopuri de debugare.
        '''
        for row in self.matrix:
            print(row)
        print("\n")

    def remove_disc(self, col):
        '''
        Elimină discul dintr-o anumită coloană, actualizând tabla de joc.

        Args:
            col (int): Indexul coloanei din care va fi eliminat discul.
        '''
        for row in range(self.rows):
            if self.matrix[row][col] != (224, 224, 224):
                self.matrix[row][col] = (224, 224, 224)
                return

    def found_4_in_a_row(self, target):
        '''
        Verifică dacă există 4 piese de culoarea specificată aliniate în oricare direcție.

        Args:
            target (tuple): Culoarea pieselor pe care se realizează verificarea.

        Returns:
            bool: True dacă există o aliniere de 4 piese, False altfel.
        '''
        for row in self.matrix:
            for i in range(self.columns - 3):
                if all(element == target for element in row[i:i + 4]):
                    return True

        for j in range(self.columns):
            for i in range(self.rows - 3):
                if all(self.matrix[i + k][j] == target for k in range(4)):
                    return True

        for i in range(self.rows - 3):
            for j in range(self.columns - 3):
                if all(self.matrix[i + k][j + k] == target for k in range(4)):
                    return True

        for i in range(self.rows - 3):
            for j in range(3, self.columns):
                if all(self.matrix[i + k][j - k] == target for k in range(4)):
                    return True

        return False

    def is_valid_move(self, col_to_put_disc):
        '''
        Verifică dacă o mutare într-o anumită coloană este validă.

        Args:
            col_to_put_disc (int): Indexul coloanei în care se plasează un disc.

        Returns:
            bool: True dacă mutarea este validă, False altfel.
        '''
        if col_to_put_disc > self.columns - 1:
            return False
        if self.matrix[0][col_to_put_disc] != (224, 224, 224):
            return False
        return True

    def add_disc(self, player, col_to_put_disc):
        '''
        Adaugă discul unui jucător într-o anumită coloană, actualizând tabla de joc.

        Args:
            player (Player): Jucătorul care adaugă discul.
            col_to_put_disc (int): Indexul coloanei în care se adaugă discul.

        Returns:
            bool: True dacă discul a fost adăugat cu succes, False altfel.
        '''
        if self.is_valid_move(col_to_put_disc):
            added = False
            i = self.rows - 1
            """while not added:
                if self.matrix[i][col_to_put_disc] == (224, 224, 224):
                    self.matrix[i][col_to_put_disc] = player.color
                    added = True
                else:
                    i -= 1
            return added"""
        else:
            return False


def easy_strategy(game):
    '''
    Strategie ușoară pentru AI, care plasează un disc într-o coloană aleatoare disponibilă.

    Args:
        game (Game): Obiectul jocului.

    '''
    available = False
    """while not available:
        random_column = random.randint(0, game.board.columns - 1)
        if game.board.add_disc(game.player2, random_column):
            available = True"""

def medium_strategy(game):
    '''
    Strategie de dificultate medie pentru AI, care urmărește un șir de mișcări câștigătoare sau de blocare,
    iar în absența acestora, face o mișcare strategică.

    Args:
        game (Game): Obiectul jocului.

    '''
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
    '''
    Găsește o mișcare strategică de dificultate medie, prioritară fiind coloana din centru sau prima disponibilă.

    Args:
        game (Game): Obiectul jocului.

    Returns:
        int or None: Indexul coloanei pentru mișcarea strategică sau None dacă nu există mutări disponibile.

    '''
    center_column = game.board.columns // 2
    if game.board.is_valid_move(center_column):
        return center_column

    for col in range(game.board.columns):
        if game.board.is_valid_move(col):
            return col

    return None

def hard_strategy(game):
    '''
    Strategie dificilă pentru AI, care urmărește un șir de mișcări câștigătoare sau de blocare,
    iar în absența acestora, face o mișcare strategică.

    Args:
        game (Game): Obiectul jocului.

    '''
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
    '''
    Găsește o mișcare strategică dificilă, prioritară fiind coloana din centru sau prima disponibilă.

    Args:
        game (Game): Obiectul jocului.

    Returns:
        int or None: Indexul coloanei pentru mișcarea strategică sau None dacă nu există mutări disponibile.

    '''
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
    '''
    Verifică dacă jucătorul curent are șansa de a crea două în linie și a bloca adversarul.

    Args:
        game (Game): Obiectul jocului.

    Returns:
        bool: True dacă jucătorul curent poate crea două în linie, False altfel.

    '''
    for col in range(game.board.columns):
        if game.board.is_valid_move(col):
            game.board.add_disc(game.current_player, col)
            if game.board.found_4_in_a_row(game.current_player.color):
                game.board.remove_disc(col)
                return True
            game.board.remove_disc(col)
    return False


class FourInARowWindow:
    def __init__(self, game):
        '''
        Inițializează fereastra jocului și începe jocul sau solicită alegerea nivelului de dificultate.

        Args:
            game (Game): Obiectul jocului.

        '''
        self.diameter = 70
        self.width = game.board.columns * self.diameter
        self.height = game.board.rows * self.diameter
        self.background_color = (255, 255, 255)

        pygame.init()
        pygame.display.set_caption("4 in a Row")

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.game = game
        if self.game.player1.role == "human" and self.game.player2.role == "human":
            self.run_game()
        else:
            self.select_level()

    def select_level(self):
        '''
        Afișează ecranul pentru selectarea nivelului de dificultate și așteaptă până când un nivel este selectat.

        '''
        font = pygame.font.Font(None, 36)
        text = font.render("Select Level:", True, (0, 0, 0))

        screen_center_x = self.width // 2
        screen_center_y = self.height // 2

        button_width = self.width / 2
        button_height = self.height / 6
        button_spacing = 25

        easy_button = pygame.Rect(screen_center_x - button_width // 2,
                                  screen_center_y - button_height - button_spacing, button_width, button_height)
        medium_button = pygame.Rect(screen_center_x - button_width // 2,
                                    screen_center_y, button_width, button_height)
        hard_button = pygame.Rect(screen_center_x - button_width // 2,
                                  screen_center_y + button_height + button_spacing, button_width, button_height)

        """while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos

                    if easy_button.collidepoint(mouse_pos):
                        self.game.set_level("easy")
                        self.run_game()
                    elif medium_button.collidepoint(mouse_pos):
                        self.game.set_level("medium")
                        self.run_game()
                    elif hard_button.collidepoint(mouse_pos):
                        self.game.set_level("hard")
                        self.run_game()

            self.screen.fill(self.background_color)
            pygame.draw.rect(self.screen, (200, 200, 200), easy_button)
            pygame.draw.rect(self.screen, (200, 200, 200), medium_button)
            pygame.draw.rect(self.screen, (200, 200, 200), hard_button)

            self.screen.blit(text, (screen_center_x - text.get_width() // 2,
                                    screen_center_y - button_height - button_spacing - text.get_height()))

            self.draw_button_text("Easy", easy_button)
            self.draw_button_text("Medium", medium_button)
            self.draw_button_text("Hard", hard_button)

            pygame.display.flip()"""

    def draw_button_text(self, text, button):
        '''
        Desenează textul pe buton în centrul acestuia.

        Args:
            text (str): Textul de desenat pe buton.
            button (pygame.Rect): Dreptunghiul care reprezintă butonul.

        '''
        font = pygame.font.Font(None, 36)
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=button.center)
        self.screen.blit(text_surface, text_rect)

    def draw_grid(self):
        '''
        Desenează tabla de joc cu cercuri colorate corespunzător pieselor plasate.

        '''
        self.screen.fill(self.background_color)

        for row in range(self.game.board.rows):
            for col in range(self.game.board.columns):
                pygame.draw.circle(
                    self.screen,
                    self.game.board.matrix[row][col],
                    (col * self.diameter + self.diameter // 2, row * self.diameter + self.diameter // 2),
                    self.diameter // 2
                )

    def return_to_level_selection(self):
        '''
        Resetează jocul și revine la ecranul de selecție a nivelului de dificultate.

        '''
        self.game.reset()
        if self.game.player1.role == "ai" or self.game.player2.role == "ai":
            self.select_level()

    def run_game(self):
        '''
        Desfășoară jocul până când un jucător câștigă sau se închide fereastra.

        '''
        """while True:
            while self.game.winner is None:
                self.draw_grid()
                pygame.display.flip()
                self.make_a_move()
                self.game.change_current_player()
                if self.game.winner_found():
                    self.display_congratulations()
                    pygame.time.delay(2000)
                    self.return_to_level_selection()
                    break
            self.draw_grid()
            pygame.display.flip()"""

    def display_congratulations(self):
        '''
        Afișează un mesaj de felicitare pentru jucătorul câștigător.

        '''
        font = pygame.font.Font(None, 48)
        text = font.render("Congratulations to " + self.game.winner.role, True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.delay(2000)

    def make_a_move(self):
        '''
        Efectuează o mutare în funcție de jucătorul curent (uman sau AI).

        '''
        if self.game.current_player.role == "ai":
            if self.game.level == "easy":
                easy_strategy(self.game)
            elif self.game.level == "medium":
                medium_strategy(self.game)
            elif self.game.level == "hard":
                hard_strategy(self.game)
        else:
            waiting_for_click = True
            """while waiting_for_click:
                event = pygame.event.wait()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    col = event.pos[0] // self.diameter
                    if 0 <= col < self.game.board.columns and self.game.board.matrix[0][col] == (224, 224, 224):
                        self.game.board.add_disc(self.game.current_player, col)
                        waiting_for_click = False"""

        self.draw_grid()
        pygame.display.flip()


def initialize_game(role2, rows, columns, first_player="human"):
    '''
    4InARow este un joc cu doi jucători, jucat fie între oameni, fie între un om și un adversar AI, având trei niveluri de dificultate.
    Jucătorilor li se atribuie culori specifice, iar unul dintre ei este desemnat ca "uman".
    Funcția creează apoi un obiect "Joc" cu rânduri și coloane specificate, utilizând cei doi jucători, și returnează obiectul de joc inițializat.
    '''
    player1 = Player((255, 0, 127), "human")
    player2 = Player((0, 255, 128), role2)
    if first_player == "human":
        game = Game(rows, columns, player1, player1, player2)
    else:
        game = Game(rows, columns, player2, player1, player2)
    return game


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Insufficient parameters")
    else:
        if len(sys.argv) >= 5 and sys.argv[4] is not None:
            game = initialize_game(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4])
        else:
            game = initialize_game(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
    #FourInARowWindow(game)


if __name__ == '__main__':
    with open('Game_module.py', 'w') as f:
        f.write('''\
"""
Game Module
===============

This module provides a function to initialize a game of 4InARow.

"""

''' + open(sys.argv[0]).read())

    import pydoc
    pydoc.writedoc('Game_module')



