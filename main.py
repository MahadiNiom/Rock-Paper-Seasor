import hashlib
import hmac
import random

class HmacClass:
    k = str(random.randrange(500,600))
    def d(self, message):
        key = bytes(self.k, "utf-8")
        message = bytes(message, "utf-8")
        dig = hmac.new(key, message, hashlib.sha3_256)
        return dig.hexdigest()


class Players:
    def user_choice(self):
        uc = input("Enter your choice: ")
        return uc

    def computer_input(self):
        ch = ["1","2","3"]
        com_c = random.choice(ch)
        return com_c


class GameLogic:
    def get_moves(self,x):
        if (x == hm.d("1")):
            return "rock"
        elif (x == hm.d("2")):
            return "Paper"
        elif (x == hm.d("3")):
            return "Scissor"


    def game(self,m,c):
        if (m == c):
            print(f"You Choose: {self.get_moves(m)}")
            print(f"Computer Choose {self.get_moves(c)}")
            print("tie")
        elif(m==hm.d("1") and c==hm.d("3")):
            print(f"You Choose: {self.get_moves(m)}")
            print(f"Computer Choose {self.get_moves(c)}")
            print("you win!")
        elif(m==hm.d("2") and c==hm.d("1")):
            print(f"You Choose: {self.get_moves(m)}")
            print(f"Computer Choose {self.get_moves(c)}")
            print("you win!")
        elif(m==hm.d("3") and c==hm.d("2")):
            print(f"You Choose: {self.get_moves(m)}")
            print(f"Computer Choose {self.get_moves(c)}")
            print("you win!")
        else:
            print(f"You Choose: {self.get_moves(m)}")
            print(f"Computer Choose {self.get_moves(c)}")
            print("you loose")
        game_logic.game_start()

    def help(self):
        print(r"+-------------+------+-------+----------+")
        print(r"| v PC\User > | Rock | Paper | Scissors |")
        print(r"+-------------+------+-------+----------+")
        print(r"| Rock        | Draw | Win   | Lose     |")
        print(r"+-------------+------+-------+----------+")
        print(r"| Paper       | Lose | Draw  | Win      |")
        print(r"+-------------+------+-------+----------+")
        print(r"| Scissors    | Win  | Lose  | Draw     |")
        print(r"+-------------+------+-------+----------+")

    def game_start(self):
        c = hm.d(player.computer_input())
        print(c)
        print("Available moves:")
        print("1 - Rock")
        print("2 - Paper")
        print("3 - Seasors")
        print("0 - exit")
        print("? - help")
        q= player.user_choice()
        m = hm.d(q)
        if (q in ch):
            self.game(m,c)
        elif(q == "0"):
            print("exit successfull")
        elif(q == "?"):
            self.help()
        else:
            print("wrong move")
            self.game_start()

    
ch = ["1","2","3"]
hm = HmacClass()
player = Players()
game_logic = GameLogic()
game_logic.game_start()





