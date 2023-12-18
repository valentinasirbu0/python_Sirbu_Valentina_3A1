import pygame
import sys

class FourInARowWindow:
    def __init__(self, game):
        self.diameter = 70
        self.width = game.board.columns * self.diameter
        self.height = game.board.rows * self.diameter
        self.background_color = (224, 224, 224)
        self.disc_color = (255, 255, 255)

        pygame.init()
        pygame.display.set_caption("4 in a Row")

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.game = game
        self.run_game()

    def draw_grid(self):
        self.screen.fill(self.background_color)

        for row in range(self.game.board.rows):
            for col in range(self.game.board.columns):
                pygame.draw.rect(self.screen, self.disc_color,
                                 (col * self.diameter, row * self.diameter, self.diameter, self.diameter))

                cell_color = self.game.board.matrix[row][col]
                pygame.draw.circle(self.screen, cell_color,
                                   (col * self.diameter + self.diameter // 2, row * self.diameter + self.diameter // 2),
                                   self.diameter // 2)

    def handle_mouse_click(self, col):
        for row in range(self.game.board.rows - 1, -1, -1):
            if self.game.board[row][col] == ' ':
                self.game.board[row][col] = self.game.current_player.color
                self.game.change_current_player()
                break  # Break after making a move

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    col = event.pos[0] // self.diameter
                    if 0 <= col < self.game.board.columns and self.game.board[0][col] == ' ':
                        self.handle_mouse_click(col)

            self.draw_grid()
            pygame.display.flip()


