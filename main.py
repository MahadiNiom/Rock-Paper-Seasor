import hashlib, hmac, random,sys

class HmacClass:
        
    def Calc_digest(self,key, message):
        k = bytes(str(key), "utf-8")
        message = bytes(message, "utf-8")
        dig = hmac.new(k, message, hashlib.sha3_256)
        return dig.hexdigest()
    


class Moves:
    mx = ["rock","paper", "scissor", "lizard", "spoke","6th","7th"]

    def mk_mv(self,x, moves):
        mv = {}
        for i in range(x):
            try:
                mv[moves[i]] = i+1
            except IndexError:
                print("not in list")
        return mv

    def mk_cm(self,moves):
        arr = list()
        for key, values in moves.items():
            arr.append(key)
        c = random.choice(arr)
        return c

    def mk_um(self, x, m):
        if x in m.values():
            for key , value in m.items():
                if value == x:
                    print(f"you chose: {key}")
                    return key

    def mk_uin1(self):
        while True:
            try:
                num = int(input("Please enter an odd integer greater than 1: "))
                if num > 1 and num % 2 != 0:
                    return num
                else:
                    print("Invalid input! Please enter an odd integer greater than 1.")
            except ValueError:
                print("Invalid input! Please enter a valid integer.")

    def mk_uin2(self,val):
        while True:
            try:
                user = input("enter your move").replace(" ", "")
                if user == "0":
                    print("exit Successfull")
                    sys.exit()
                elif user == "?":
                    return user
                elif int(user) in val.values():
                    return int(user)
            except ValueError:
                print("Wrong move")
            

class Game:
    def winner(self,m,c, moves):
        if (moves[m]%2 == 0) and (moves[c]%2 == 0):
            if moves[m] == moves[c]:
                return "tie"
            elif moves[m] > moves[c]:
                return "lose"
            elif moves[m] < moves[c]:
                return "win"
        elif (moves[m]%2 == 1) and (moves[c]%2 == 1):
            if moves[m] == moves[c]:
                return "tie"
            elif moves[m] > moves[c]:
                return "lose"
            elif moves[m] < moves[c]:
                return "win"
        else:
            if moves[m] == moves[c]:
                return "tie"
            elif moves[m] < moves[c]:
                return "lose"
            elif moves[m] > moves[c]:
                return "win"
    
    def create_table(self,data):
        column_widths = [max(len(str(item)) for item in col) for col in zip(*data)]
        table = ''
        for row in data:
            table += '| ' + ' | '.join(str(item).ljust(width) for item, width in zip(row, column_widths)) + ' |\n'
        
        separator = '+-' + '-+-'.join('-' * width for width in column_widths) + '-+\n'
        
        table_with_separator = separator + table + separator
        
        return table_with_separator
    
            

    def help(self,a):
        print("help")
        l = len(a)
        arr = [[0 for _ in range(l)] for _ in range(l)]
        for key1, value1 in a.items():
            for key2, value2 in a.items():
                arr[value1-1][value2-1] = self.winner(key1,key2,a)
        for k,v in a.items():
            arr[v-1].insert(0,k)
        hed = [0 for _ in range(len(arr[0]))]
        arr.insert(0, hed)
        for k,v in a.items():
            arr[0][v] = k
        arr[0][0] = "v PC/User >"
        print(self.create_table(arr))
        




    def game(self):
        k = random.randrange(200,600)
        h= HmacClass()
        m = Moves()
        moves = ["rock","paper", "scissor", "lizard", "spoke","6th","7th"]
        n = m.mk_uin1()
        a_mv = m.mk_mv(n,moves)
        c = m.mk_cm(a_mv)
        print(h.Calc_digest(k,c))
        print("Available Moves")
        for key, values in a_mv.items():
            print(key," "*(9-len(key)),values)
        print("Exit - 0")
        print("Help - ?")
        uin = m.mk_uin2(a_mv)
        if uin == "?":
            self.help(a_mv)
            self.game()
        else:
            u = m.mk_um(uin,a_mv)
        print(f"computer Choose {c}")
        print(self.winner(u,c,a_mv))
        self.game()




gm = Game()
gm.game()
