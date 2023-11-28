import random
import time


class Player:

    def __init__(self):
        self.name = ''
        self.symbol = ''


class TicTacToe:
    def __init__(self):
        self.board = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9']
        ]
        self.p1 = Player()
        self.p2 = Player()
        self.turn_player = None
        self.ai_hum = None

    def create_board(self):

        print('\n' + '#=' * 30 + '\n')

        print(('+' + '-' * 5) * 3 + '+')
        for row in self.board:
            print('|  ' + '  |  '.join(row) + '  |')
            print(('+' + '-' * 5) * 3 + '+')

    def available_positions(self):
        return [str(self.board[i][j]) for i in range(3) for j in range(3) if self.board[i][j] not in ['X', 'O']]

    def play_mode(self):
        modes = [0, 1]
        while True:
            try:
                mode = input("\nDo you want to play against AI(1) or Multiplayer(2):\nType '0' or '1': ")
                return modes[int(mode)]
            except:
                print("Please only enter 0(AI) or 1(Multiplayer)")

    def decide_player(self):
        self.ai_hum = self.play_mode()
        if self.ai_hum == 1:
            self.p1.name = input("Enter Player1 Name: ").title()
            self.p1.symbol = input("Enter Player1 symbol('X', 'O'): ").upper()

            self.p2.name = input("Enter Player2 Name: ").title()
            self.p2.symbol = 'O' if self.p1.symbol == 'X' else 'X'
        elif self.ai_hum == 0:
            self.p1.name = input("Enter Your Name: ").title()
            self.p1.symbol = input("Enter Your symbol('X', 'O'): ").upper()

            self.p2.name = 'Computer'
            self.p2.symbol = 'O' if self.p1.symbol == 'X' else 'X'

        print("Let's do a toss")
        self.turn_player = random.choice((self.p1, self.p2))

    def play_turn(self):
        while True:
            print(f"\nTurn: {self.turn_player.name} ({self.turn_player.symbol})\n")
            time.sleep(2)
            if self.ai_hum == 0 and self.turn_player == self.p2:
                choice = int(random.choice(self.available_positions()))
            else:
                choice = input('Enter Your choice(out of the shown numbers): ')

            try:
                row_index = (int(choice) - 1) // 3
                col_index = (int(choice) - 1) % 3
                if str(choice) in self.board[row_index]:
                    self.board[row_index][col_index] = self.turn_player.symbol
                    if self.is_win():
                        return
                    self.turn_player = self.p1 if self.turn_player == self.p2 else self.p2
                    self.create_board()
                else:
                    raise
            except:
                print("Please Enter a number out of those shown on the board")

    def is_win(self):
        for row in self.board:
            if all(elem == row[0] for elem in row):
                self.find_winner(row[0])
                return True

        for i in range(0, len(self.board)):
            if all(row[i] == self.board[0][i] for row in self.board):
                self.find_winner(self.board[0][i])
                return True

        if all(self.board[i][i] == self.board[0][0] for i in range(0, len(self.board))):
            self.find_winner(self.board[0][0])
            return True

        if all(self.board[i][3 - 1 - i] == self.board[0][2] for i in range(0, len(self.board))):
            self.find_winner(self.board[0][2])
            return True

        if not self.available_positions():
            print("Draw")
            return True

    def find_winner(self, sym):
        players = [self.p1, self.p2]
        winner = next((p for p in players if p.symbol == sym))
        print(f"{winner.name} ({winner.symbol}) Wins!")


t = TicTacToe()
t.decide_player()
t.create_board()
t.play_turn()
