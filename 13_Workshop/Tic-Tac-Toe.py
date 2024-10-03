import numpy as np

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class Board:
    def __init__(self):
        self.board = np.full((3, 3), ' ')

    def display(self):
        for row in self.board:
            print(' | '.join(row))
            print('--|---|--')

    def is_position_free(self, position):
        row, col = divmod(position - 1, 3)
        return self.board[row, col] == ' '

    def update(self, position, symbol):
        row, col = divmod(position - 1, 3)
        if self.is_position_free(position):
            self.board[row, col] = symbol
            return True
        return False

    def check_winner(self, symbol):
        for i in range(3):
            if np.all(self.board[i, :] == symbol) or np.all(self.board[:, i] == symbol):
                return True

        if np.all(np.diag(self.board) == symbol) or np.all(np.diag(np.fliplr(self.board)) == symbol):
            return True

        return False

    def is_full(self):
        return not np.any(self.board == ' ')


class Game:
    def __init__(self):
        self.board = Board()
        self.player_one = None
        self.player_two = None
        self.current_player = None

    def setup(self):
        player_one_name = input("Player 1, enter your name: ")
        player_two_name = input("Player 2, enter your name: ")

        symbol = input(f"{player_one_name}, do you want to be 'X' or 'O'? ").upper()
        while symbol not in ['X', 'O']:
            symbol = input(f"Please choose either 'X' or 'O': ").upper()

        self.player_one = Player(player_one_name, symbol)
        self.player_two = Player(player_two_name, 'O' if symbol == 'X' else 'X')

        self.current_player = self.player_one

        print(f"{self.player_one.name} is {self.player_one.symbol}")
        print(f"{self.player_two.name} is {self.player_two.symbol}")
        print("Game starts!")
        self.board.display()

    def switch_player(self):
        self.current_player = self.player_two if self.current_player == self.player_one else self.player_one

    def play_turn(self):
        while True:
            try:
                position = int(input(f"{self.current_player.name}, choose a position (1-9): "))
                if 1 <= position <= 9:
                    if self.board.update(position, self.current_player.symbol):
                        break
                    else:
                        print("This position is already taken. Try again.")
                else:
                    print("Please choose a number between 1 and 9.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        self.board.display()

    def check_game_over(self):
        if self.board.check_winner(self.current_player.symbol):
            print(f"{self.current_player.name} wins!")
            return True
        if self.board.is_full():
            print("It's a tie!")
            return True
        return False

    def start(self):
        self.setup()

        while True:
            self.play_turn()
            if self.check_game_over():
                break
            self.switch_player()


if __name__ == "__main__":
    game = Game()
    game.start()
