class TicTacToeGame():

    def __init__(self):
        self.tictacs = ['<0>', '<1>', '<2>', '<3>', '<4>', '<5>', '<6>', '<7>', '<8>']
        self.game_over = False
        self.turn = 1


    def ticky(self):
        while self.game_over == False:
            self.take_turn()

    def test_move(self, position):
        try:
            pos = int(position)
        except:
            print('Not a number')
            return False
        else:
            if pos > 8 or pos < 0:
                print('No such position; try again')
                return False
            elif self.tictacs[pos] == 'X' or self.tictacs[pos] == 'O':
                print('This position has already been taken!  Try again.')
                return False
            else:
                return True


    def take_turn(self):
        self.display_board()
        if self.turn % 2 == 0:
            player = 'X'
            position = input('where would you like to put your X?')
        else:
            player = 'O'
            position = input('where would you like to put your O?')
        if self.test_move(position):
            self.tictacs[int(position)] = player
            self.turn += 1
            if self.check_win():
                print(f'Yay! "{player}" won!')
                self.game_over = True
        else:
            self.take_turn()

    def check_win(self):
        if self.tictacs[0] == self.tictacs[1] and self.tictacs[1] == self.tictacs[2]:
            return True
        elif self.tictacs[3] == self.tictacs[4] and self.tictacs[4] == self.tictacs[5]:
            return True
        elif self.tictacs[6] == self.tictacs[7] and self.tictacs[7] == self.tictacs[8]:
            return True
        elif self.tictacs[0] == self.tictacs[3] and self.tictacs[3] == self.tictacs[6]:
            return True
        elif self.tictacs[1] == self.tictacs[4] and self.tictacs[4] == self.tictacs[7]:
            return True
        elif self.tictacs[2] == self.tictacs[5] and self.tictacs[5] == self.tictacs[8]:
            return True
        elif self.tictacs[0] == self.tictacs[4] and self.tictacs[4] == self.tictacs[8]:
            return True
        elif self.tictacs[2] == self.tictacs[4] and self.tictacs[4] == self.tictacs[6]:
            return True
        else:
            return False

    def display_board(self):
        print(f'{self.tictacs[0]} | {self.tictacs[1]} | {self.tictacs[2]}\n---------------\n{self.tictacs[3]} | {self.tictacs[4]} | {self.tictacs[5]}\n---------------\n{self.tictacs[6]} | {self.tictacs[7]} | {self.tictacs[8]}')