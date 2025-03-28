import pygame


class Player:
    def __init__(self, symbol):
        self.symbol = symbol


class Board:

    def __init__(self):
        self.cells = [[None, None, None], [None, None, None], [None, None, None]]

    def draw_grid(self, screen):
        line_color = (255, 255, 255)
        pygame.draw.line(screen, line_color, (0, 200), (600, 200), 1)
        pygame.draw.line(screen, line_color, (0, 400), (600, 400), 1)
        pygame.draw.line(screen, line_color, (200, 0), (200, 600), 1)
        pygame.draw.line(screen, line_color, (400, 0), (400, 600), 1)

    def check_winner(self, player):
        arr = self.cells
        s = player.symbol

        # Horizontal
        if arr[0][0] == arr[0][1] == arr[0][2] == s:
            return True
        elif arr[1][0] == arr[1][1] == arr[1][2] == s:
            return True
        elif arr[2][0] == arr[2][1] == arr[2][2] == s:
            return True

        # Vertical
        elif arr[0][0] == arr[1][0] == arr[2][0] == s:
            return True
        elif arr[0][1] == arr[1][1] == arr[2][1] == s:
            return True
        elif arr[0][2] == arr[1][2] == arr[2][2] == s:
            return True

        # Diagonal
        elif arr[0][0] == arr[1][1] == arr[2][2] == s:
            return True
        elif arr[0][2] == arr[1][1] == arr[2][0] == s:
            return True

        return False


class TicTacToe:
    def __init__(self):
        pygame.init()
        self.WIDTH, self.HEIGHT = 600, 600
        self.BG_COLOR = (0, 0, 0)
        self.TEXT_COLOR = (65, 105, 225)
        self.CIRCLE_COLOR = (255, 255, 255)
        self.LINE_COLOR = (255, 255, 255)
        self.LINE_WIDTH = 10

        self.font = pygame.font.SysFont("Arial", 70)
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Tic-Tac-Toe")
        self.clock = pygame.time.Clock()
        self.FPS = 300

        self.board = Board()
        self.player_x = Player('X')
        self.player_o = Player('O')
        self.current_player = self.player_x
        self.running = True
        self.game_over = False
        self.draw = False
        self.count = 0

    def sketch_X(self, x, y):
        start_pos = (x - 60, y - 60)
        end_pos = (x + 60, y + 60)
        pygame.draw.line(self.screen, self.LINE_COLOR, start_pos, end_pos, self.LINE_WIDTH)

        start_pos = (x - 60, y + 60)
        end_pos = (x + 60, y - 60)
        pygame.draw.line(self.screen, self.LINE_COLOR, start_pos, end_pos, self.LINE_WIDTH)

    def sketch_O(self, x, y):
        pygame.draw.circle(self.screen, self.CIRCLE_COLOR, (x, y), 60, self.LINE_WIDTH)

    def click(self):
        p_x, p_y = pygame.mouse.get_pos()
        col = p_x // 200
        row = p_y // 200

        # Prevent out-of-bounds clicks
        if row >= 3 or col >= 3:
            return

        if self.board.cells[row][col] is None and not self.game_over:
            self.board.cells[row][col] = self.current_player.symbol
            self.count += 1

            if self.board.check_winner(self.current_player):
                self.game_over = True
            elif self.count == 9:
                self.draw = True
                self.game_over = True
            else:
                self.current_player = self.player_o if self.current_player == self.player_x else self.player_x

    def display_winner(self):
        if self.draw:
            text_surface = self.font.render("It's a draw!!!", True, self.TEXT_COLOR)
        else:
            text_surface = self.font.render(f"Player {self.current_player.symbol} wins!!!!", True, self.TEXT_COLOR)

        text_rect = text_surface.get_rect(center=(300, 300))
        pygame.draw.rect(self.screen, (255, 255, 255), text_rect.inflate(20, 20))
        self.screen.blit(text_surface, text_rect)

    def run(self):
        while self.running:
            self.screen.fill(self.BG_COLOR)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
                    self.click()

            if self.game_over:
                self.display_winner()
            else:
                self.board.draw_grid(self.screen)
                for row in range(3):
                    for col in range(3):
                        x, y = col * 200 + 100, row * 200 + 100
                        if self.board.cells[row][col] == 'X':
                            self.sketch_X(x, y)
                        elif self.board.cells[row][col] == 'O':
                            self.sketch_O(x, y)

            pygame.display.flip()
            self.clock.tick(self.FPS)

        pygame.quit()

game = TicTacToe()
game.run()