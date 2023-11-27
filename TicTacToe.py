player, computer = "X", "O"

#Win Conditions
winner = (
    (0,1,2),
    (3,4,5),
    (6,7,8),
    (0,4,8),
    (2,4,6),
    (0,3,6),
    (1,4,7),
    (2,5,8)
)

class TicTacToe:

    def __init__(self):
        self.board = [" "] * 9

    def print_board(self):
        for i, val in enumerate(self.board):
            end_board = " | "

            # If end of board of 1st row
            # Or if end of board of 2nd row
            # Then create new line of board
            if i == 2 or i == 5:
                end_board = "\n------------\n"
            elif i == 8:
                end_board = "\n"

            # print(val, end=end) prints the current value (val) with the specified end parameter
            # Depending on the conditions, end will either be " | ", "\n------------\n", or "\n".
            # This controls how the TicTacToe board is formatted in the output.
            print(val, end=end_board)

    def can_move(self, move):
        # If move input by player is number 1-9 and it is empty
        if move in range(1, 10) and self.board[move-1] == " ":
            return True
        return False

    def can_win(self, player):
        for i in winner:
            win = True
            for idx in i:
                if self.board[idx] != player:
                    win = False
                    break
            if win:
                break
        return win

    def make_move(self, player, move):
        # Checks if player can move
        if self.can_move(move):
            self.board[move-1] = player

            #If move causes player to win, return win condition
            win = self.can_win(player)
            return (True, win)
        return (False, False)

    def computer_move(self):
        # Computer's automatic move for tictactoe
        for i in (5,1,3,7,9,2,4,6,8):
            if self.can_move(i):
                return self.make_move(computer, i)
        return self.make_move(computer, -1)

    def play(self):
        print("Index positions are: \n 1 2 3 \n 4 5 6 \n 7 8 9")
        print(f"player is {player}, computer is {computer}")

        result = "Tie"
        while True:
            # If board is completely filled, then break cause Tie
            if self.board.count(player) + self.board.count(computer) == 9:
                break

            self.print_board()

            move = int(input("Make your move [1-9]: "))
            moved, won = self.make_move(player, move)
            if not moved:
                print("Try again!")
                continue

            if won:
                result = "You win!"
                break

            _, won = self.computer_move()
            if won:
                result = "You lose!"
                break

        self.print_board()
        print(result)

game = TicTacToe()
game.play()