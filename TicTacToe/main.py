import os

def clear():
    os.system("cls")

class Player:
    def __init__(self) :
        self.name = ""
        self.symbol = ""

    def choose_name(self) :
        while True :
            name = input("please enter your name (letters only)")
            if name.isalpha():
                self.name = name
                break
            else :
                print("Invalid name, please use letters only")

    def choose_symbol(self) :
        while True :
            symbol = input(f"{self.name} choose your symbol (X-O) prefered, please use one letter only")
            if symbol.isalpha() and len(symbol) == 1 :
                self.symbol = symbol.upper()
                break
            else :
                print("Invalid, please try again")

class Menu:
    valid = ("1", "2")
    def display_main_menu(self):
        print("Welcom to TicTacToe game AKA (X-O)")
        print("----------------------------------")
        print("1. Start Game")
        print("2. Quit Game")
        while True:
            choice = input("Enter your choice (1-2)")
            if choice not in Menu.valid :
                print("invalid choice, please choose (1) or (2)")
            else :
                return choice
    def display_endgame_menu(self):
        menu_text = """
Game Over!
1. Restart Game
2. Quit Game
Enter your choice (1-2)
"""
        while True:
            choice = input(menu_text)
            if choice not in Menu.valid :
                print("invalid choice, please choose (1) or (2)")
            else :
                return choice
            
class Board:
    def __init__(self):
        self.board = [str(x) for x in range(1, 10)]
    
    def display_board(self):
        for i in range(0,9,3) :
            print("|".join(self.board[i:i+3]))
            if i < 6 :
                print("-----")
    
    def update_board(self, choice, symbol) :
        if self.is_valid_move(choice):
            self.board[choice - 1] = symbol
            return True
        return False

    def is_valid_move(self, choice):
        return self.board[choice - 1].isdigit()
    
    def current_valid_move(self):
        print("current valid spots are : ", end= " ")
        for x in self.board:
            if x.isdigit() :
                print(x, end= " ")

    def reset_board(self):
        self.board = [str(x) for x in range(1, 10)]

class Game:
    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0

    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == "1":
            self.setup_players()
            self.play_game()

        else :
            self.quit_game()
    
    def setup_players(self):
        for index, player in enumerate(self.players, start=1):
            print(f"player{index} :")
            player.choose_name()
            player.choose_symbol()
            print("-"*20)
            clear()

    def play_game(self):
        while True:
            self.player_turn()
            if self.check_win() or self.check_draw():
                self.board.display_board()
                choice = self.menu.display_endgame_menu()
                if choice == "1" :
                    self.restart_game()
                else:
                    self.quit_game()
                    break
            clear()

    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        self.play_game()
        
    
    def check_win(self):
        win_combination = [
            [0,1,2], [3,4,5], [6,7,8], #rows
            [0,3,6], [1,4,7], [2,5,8], #columns
            [0,4,8], [2,4,6]           #diagonal
        ]

        for combo in win_combination:
            if (self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]]):
                return True
        return False

    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)

    def player_turn(self):
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"{player.name}'s turn ({player.symbol})")
        while True:
            try :
                cell_choice = int(input("choose cell (1-9)"))
                if 1 <= cell_choice <= 9 and self.board.update_board(cell_choice, player.symbol):
                    break
                else :
                    print("Invalid Move!!, try again")
            except ValueError:
                print("please enter number 1-9")
        self.switch_player()
    

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def quit_game(self):
        print("Thank you for playing....!")
game = Game()
game.start_game()