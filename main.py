import hashlib, hmac, random
        
class GameClass:
    key = str(random.randrange(500,600))
    def Calc_digest(self, message):
        key = bytes(self.key, "utf-8")
        message = bytes(message, "utf-8")
        dig = hmac.new(key, message, hashlib.sha3_256)
        return dig.hexdigest()

    def get_userinput1(self):
        px = None
        while (px == None):
            try:
                px =int(input("Enter an odd integer number: "))
            except ValueError:
                print("Not an odd integer number")
        return px
    
    def make_userinput1(self):
        u_in1 = self.get_userinput1()
        if ((u_in1 % 2) == 0):
            print("Not an odd integer number")
            u_in1 = self.get_userinput1()
        else:
            pass
        return u_in1

    def available_moves(self, x):
        arr = list()
        for y in range(x):
            arr += [y+1]
        return arr
    
    def winning_move(self, m, c):
        if ((m % 2) == 1) and (c % 2 == 1):
            r = min(m,c)
        elif((m % 2)== 0) and (c %2 ==0):
            r = min(m,c)
        else:
            r = max(m,c)
        return r
    def game(self,m,c,w):
        if (m == w) and (c == w):
            print("tie")
        elif c == w:
            print("computer wins")
        elif m == w:
            print("you win")

    def create_table(self,data):
        column_widths = [max(len(str(item)) for item in col) for col in zip(*data)]
        table = ''
        for row in data:
            table += '| ' + ' | '.join(str(item).ljust(width) for item, width in zip(row, column_widths)) + ' |\n'
        
        separator = '+-' + '-+-'.join('-' * width for width in column_widths) + '-+\n'
        
        table_with_separator = separator + table + separator
        
        return table_with_separator

    def help(self,ch):
        ch = ch
        l = len(ch)
        arr = [[0 for _ in range(l)] for _ in range(l)]
        for i in ch:
            for j in ch:
                if (i%2 == 1) and (j%2 == 1):
                    if i == j:
                        arr[i-1][j-1]= "tie"
                    elif i<j:
                        arr[i-1][j-1] = "lose"
                    elif i>j:
                        arr[i-1][j-1] = "win"
                elif(i%2 == 0) and (j%2 == 0):
                    if i == j:
                        arr[i-1][j-1]= "tie"
                    elif i<j:
                        arr[i-1][j-1] = "lose"
                    elif i>j:
                        arr[i-1][j-1] = "win"
                else:
                    if i == j:
                        arr[i-1][j-1]= "tie"
                    elif i<j:
                        arr[i-1][j-1] = "win"
                    elif i>j:
                        arr[i-1][j-1] = "lose"

        for i in ch:
            arr[i-1].insert(0,i)

        ch.insert(0, "v PC/User >")
        arr.insert(0,ch)
        table = self.create_table(arr)
        print(table)



    def players_move(self,c,ch):
        m = input("Enter your move: ")
        try:
            m = int(m)
        except ValueError:
            if m == "?":
                self.help(ch)
            else:
                print("wrong move")

        if type(m) == str:
            pass
        elif type(m) == int:
            if m in (ch):
                w = self.winning_move(m,c)
                self.game(m,c,w)
            else:
                print("move not available")


g = GameClass()

ch = g.available_moves(g.make_userinput1())
c= random.choice(ch)
print(g.Calc_digest( str(c)))
print("available moves are")
for i in ch:
    print(f"move - {i}")
print("Exit - 0")
print("Help - ?")
g.players_move(c,ch)
print("computer choose: ",c)
