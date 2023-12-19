import pygame
import sys
import Strategies


class FourInARowWindow:
    def __init__(self, game):
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

        while True:
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

            pygame.display.flip()

    def draw_button_text(self, text, button):
        font = pygame.font.Font(None, 36)
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=button.center)
        self.screen.blit(text_surface, text_rect)

    def draw_grid(self):
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
        self.game.reset()
        if self.game.player1.role == "ai" or self.game.player2.role == "ai":
            self.select_level()

    def run_game(self):
        while True:
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
            pygame.display.flip()

    def display_congratulations(self):
        font = pygame.font.Font(None, 48)
        text = font.render("Congratulations to " + self.game.winner.role, True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.delay(2000)

    def make_a_move(self):
        if self.game.current_player.role == "ai":
            if self.game.level == "easy":
                Strategies.easy_strategy(self.game)
            elif self.game.level == "medium":
                Strategies.medium_strategy(self.game)
            elif self.game.level == "hard":
                Strategies.hard_strategy(self.game)
        else:
            waiting_for_click = True
            while waiting_for_click:
                event = pygame.event.wait()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    col = event.pos[0] // self.diameter
                    if 0 <= col < self.game.board.columns and self.game.board.matrix[0][col] == (224, 224, 224):
                        self.game.board.add_disc(self.game.current_player, col)
                        waiting_for_click = False

        self.draw_grid()
        pygame.display.flip()
