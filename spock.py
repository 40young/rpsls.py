from enum import Enum
import random
import time
from time import sleep
import colorama
from colorama import Fore, Back, Style


moves = ["rock", "paper", "scissors", "lizard", "Spock"]

rounds = 0
score = 0


class Player():
    def move(self):
        self.score = 0
        return moves[0]

    def learn(self, my_move, their_move):
        pass


class randomPlayer(Player):
    def move(self):
        throw = random.choice(moves)
        return (throw)


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        throw = input("rock", "paper", "scissors", "lizard", "Spock")
        while throw != 'rock' and throw != 'scissors' and throw != 'paper' \
                and throw != 'lizard' and throw != 'Spock':
            print(Fore.RED + "Invalid entry")
            return throw
        return (throw)


class Reflect(Player):
    def __init__(self):
        Player.__init__(self)
        self.learn_move = None

    def move(self):
        if self.learn_move is None:
            throw = moves[0]
        else:
            throw = self.learn_move
            return (throw)

    def learn(self, learn_move):
        self.learn_move = learn_move


class CyclePlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.step = 0

    def move(self):
        index = self.step
        if self.step < 4:
            self.step = self.step + 1
        else:
            self.step = 0
        return moves[index]


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'rock' and two == 'lizard') or
            (one == 'paper' and two == 'Spock') or
            (one == 'scissors' and two == 'lizard') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock') or
            (one == 'lizard' and two == 'Spock') or
            (one == 'lizard' and two == 'paper') or
            (one == 'Spock' and two == 'scissors') or
            (one == 'Spock' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = self.p1
        self.p2_score = self.p2

    def play_game(self):
        print(Fore.CYAN + "Your move! rock, paper, scissors,\
lizard or Spock?")
        answer = ['rock', 'paper', 'scissors', 'lizard', 'Spock']
        p2 = input('Enter value: rock, paper, scissors, lizard, Spock ')
        while p2 != 'rock' or p2 != 'paper' or p2 != 'scissors'\
                or p2 != 'lizard' or p2 != 'Spock':
            break
        Game.play_game()
        for round in range(3):
            print(f"Round {round}:")
            self.rounds()
            print(Fore.RED + "Game over!")
        if self.p1.score > self.p2.score:
            print(Fore.GREEN + '**Player 1 WINS!**')
            rounds += 1
        elif self.p1.score < self.p2.score:
            print(Fore.GREEN + '**Player 2 WINS!**')
            rounds += 1
        else:
            print(Fore.YELLOW + '**Its a DRAW!**')
            rounds += 1
        print("End Score" + str(self.p1.score) + "TO" + str(self.p2.score))

    def rounds(self):
        global rounds, p1, p2
        rounds += 1
        print("Player 1 {self.p1_score} Player 2 {self.p2_score}\
             Round: {rounds}")
        self.p1_score = self.p1
        self.p2_score = self.p2
        if p1 != p2:
            print(Fore.RED + "**Its a DRAW!**")
        elif self.p1.score > self.p2.score:
            print(Fore.GREEN + "**Player 1 WINS!**")
        else:
            print(Fore.GREEN + "**Player 2 WINS!**")

    def play(self, move1, move2):
        move1 = self.p1.move()
        move2 = self.p2.move()
        result = Game.play(move1, move2)
        print(f"You played {move1}")
        print(f"Opponent played {move2}")
        if beats(move1, move2):
            print("** PLAYER 1 WINS **")
            print(f"Score: Player 1: {move1}  Player 2: {move2}\n\n")
            self.p1.score += 1
            return 1
        elif beats(move2, move1):
            print("** PLAYER 2 WINS **")
            print(f"Score Player 1: {move1}  Player 2: {move2}\n\n")
            self.p2.score += 1
            return 2
        else:
            print("** It's A DRAW **")
            print(f"Score Player 1: {move1}  Player 2: {move2}\n\n")
            return 0


if __name__ == '__main__':
    sleep(1)
    print(Fore.MAGENTA + "Welcome to my Rock,Paper,Scissors,\
Lizard,Spock game!\n")
    print(Fore.CYAN + "The rules of the game are as follows:\n")
    print(Fore.GREEN + "Scissors cut paper")
    print(Fore.GREEN + "Paper covers rock")
    print(Fore.GREEN + "Rock crushes lizard")
    print(Fore.GREEN + "Lizard poisons Spock")
    print(Fore.GREEN + "Spock smashes scissors")
    print(Fore.GREEN + "Scissors decapitate lizard")
    print(Fore.GREEN + "Lizard eats paper")
    print(Fore.GREEN + "Paper disproves Spock")
    print(Fore.GREEN + "Spock vaporizes rock")
    print(Fore.GREEN + "Rock crushes scissors")
    print(Style.RESET_ALL)
    p1 = randomPlayer()
    p2 = HumanPlayer()
    game = Game(p1, p2)
    Game.play_game()
