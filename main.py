import random

class TicTacToe():

    def __init__(self):
        self.board = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9']
        ]
        self.player_1 = ''
        self.player_2 = ''
        self.turn_symbol = ''


    def create_board(self):
        print(('+' + '-' * 5) * 3 + '+')
        for row in self.board:
            print('|  ' + '  |  '.join(row) + '  |')
            print(('+' + '-'*5) * 3 + '+')


    def decide_player(self):
        self.player_1 = input("Enter Player1 symbol('x', 'o'): ")
        self.player_2 = input("Enter Player2 symbol('x', 'o'): ")
        print("Let's do a random toss")
        self.turn_symbol = random.choice(('x', 'o'))


    def play_turn(self):
        while True:
            print(f"\n'{self.turn_symbol}' Turn\n")
            choice = int(input('Enter Your choice(out of the shown numbers): '))
            row_index = (choice-1) // 3
            col_index = (choice-1) % 3
            if str(choice) in self.board[row_index]:
                self.board[row_index][col_index] = self.turn_symbol
                if self.is_win():
                    return
                self.turn_symbol = 'o' if self.turn_symbol == 'x' else 'x'
                print('\n' + '#=' * 30 + '\n')
                self.create_board()
            else:
                print("Please enter a number out of the numbers shown on the board.")


    def is_win(self):
        for row in self.board:
            if all(elem == row[0] for elem in row):
                print(f"'{row[0]}' is the Winner! ")
                return True

        for i in range(0, len(self.board)):
            if all(row[i] == self.board[0][i] for row in self.board):
                print(f"'{self.board[0][i]}' is the Winner! ")
                return True

        if all( self.board[i][i] == self.board[0][0] for i in range ( 0, len(self.board) ) ):
            print(f"'{self.board[0][0]}' is the Winner! ")
            return True

        if all( self.board[i][3-1-i] == self.board[0][2] for i in range( 0, len(self.board) ) ):
            print(f"'{self.board[0][2]}' is the Winner! ")
            return True


t = TicTacToe()
t.decide_player()
t.create_board()
t.play_turn()
