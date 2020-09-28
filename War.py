###########################################
### WELCOME TO The War Card Game PROJECT ##
###########################################



from random import shuffle


fd = open("results.txt","w+")
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

#---------------------------------------------------------------- Classes ------------------------------------------------------------------------------------
class Deck:
    def __init__(self):
        self.deck=[]
        for i in SUITE:
            for j in RANKS:
                if j=='J':
                    t=(i,11)
                elif j=='Q':
                    t=(i,12)
                elif j=='K':
                    t=(i,13)
                elif j=='A':
                    t=(i,14)
                else:
                    t=(i,j)
                self.deck.append(t)

    def Split(self):
        shuffle(self.deck)
        self.comp_count=int(len(self.deck)/2)
        self.com_deck=self.deck[0:self.comp_count]
        self.player_deck=self.deck[self.comp_count:]
        shuffle(self.com_deck)
        shuffle(self.player_deck)



class Hand:
    def __init__(self,card_dec):
        self.card_dec=card_dec
    def add(self,card):
        self.card_dec.append(card)
    def remove(self,card):
        self.card_dec.remove(card)

#this function will print the pair that currently in play
def str_For_print(card):
    num=int(card[1])
    if num ==11:
        fd.write(card[0]+",J")
    elif num ==12:
        fd.write(card[0]+",Q")
    elif num ==13:
        fd.write(card[0]+",K")
    elif num ==14:
        fd.write(card[0]+",A")
    else:
        fd.write(card[0]+","+card[1])

class Player:
    def __init__(self,name,hand):
        self.hand=hand

        self.name=name
    def check(self):
        if hand==[]:
            return True
        else:
            return False

######################
#### GAME PLAY #######
######################
fd.write("Welcome to War, let's begin...\n")
player_name=input("Enter your name ")
fd.write("Hello "+player_name)
fd.write("The cards that you got are:\n")
deck=Deck()
deck.Split()
for i in deck.player_deck:
    str_For_print(i)
    fd.write("\n")
fd.write("The cards that the computer got are:\n")
for i in deck.com_deck:
    str_For_print(i)
    fd.write("\n")
player_hand= Hand(deck.player_deck)
computer_hand=Hand(deck.com_deck)
computer=Player("Computer",computer_hand)
player=Player(player_name,player_hand)
#-------------------------------------------------------------- The Body --------------------------------------------------------------------------------------------
def Start_game(computer,player):
    p_deck=player.hand.card_dec
    c_deck=computer.hand.card_dec
    k=0
    #now we will iterate until one of the players is out of cars, and the other is the winner
    while not p_deck ==[] and not c_deck ==[]:
         cardA= p_deck[0]
         cardB=c_deck[0]

         if int(cardA[1]) > int(cardB[1]):
             str_For_print(cardA)
             fd.write("\n")
             str_For_print(cardB)
             fd.write("\n")
             fd.write("Player has won this round "+str(len(p_deck))+", "+str(len(c_deck))+"\n--------------\n")
             computer.hand.remove(cardB)
             player.hand.add(cardB)
         elif int(cardA[1]) < int(cardB[1]):
             str_For_print(cardA)
             fd.write("\n")
             str_For_print(cardB)
             fd.write("\n")
             fd.write("Computer has won this round "+str(len(p_deck))+", "+str(len(c_deck))+"\n--------------\n")
             computer.hand.add(cardA)
             player.hand.remove(cardA)
#in this section we will check if the two card are the Same.
#if so, we need to iterate until one of the players will have the apper hand
         else:
            know_c=False
            know_p=False
            t_p=[]
            t_c=[]
            d=0
            flag=False
            while not flag ==True and not d==1:
                i=0
                while i < 3:
                    c_len=len(c_deck)
                    p_len=len(p_deck)
                    if c_len>1 and  p_len>1:
                        t_p.append(p_deck[0])
                        player.hand.remove(p_deck[0])
                        t_c.append(c_deck[0])
                        computer.hand.remove(c_deck[0])
                    else:
                        d=1
                        if c_len ==0:
                            know_c=True
                        else:
                            know_p=True
                    i=i+1

                if not d==1:
                    val=battle(p_deck[-1],c_deck[-1])
                elif know_c==True:
                    val=battle(p_deck[-1],t_c[0])
                else:
                    val=battle(t_p[0],c_deck[-1])
                if val==1:
                    flag=True
                    for card in t_p:
                        player.hand.add(card)
                    for card in t_c:
                        player.hand.add(card)
                    t_p=[]
                    t_c=[]

                elif val ==-1:
                    flag=True
                    for card in t_c:
                        computer.hand.add(card)
                    for card in t_p:
                        computer.hand.add(card)
                    t_c=[]
                    t_p=[]
    fd.write("\n----------And the Winner is:----------\n")
    if p_deck ==[]:
        fd.write("The computer -_-")

    else:
        fd.write(player_name+ " You won!")

def battle(cardA,cardB):
    if int(cardA[1]) > int(cardB[1]):
        return 1
    elif int(cardA[1]) <int(cardB[1]):
        return -1
    else:
        return 0

fd.write("\n----------- Lets start the Game!----------------\n")
Start_game(computer,player)
fd.close()
