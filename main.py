from bke import MLAgent, is_winner, opponent, train, save
 
 # het trainen van de agent
class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward
   
 
my_agent = MyAgent()
 
train(my_agent, 3000)
 
save(my_agent, 'MyAgent_3000')


# wanneer de agent al getraind is
class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward
   
 
my_agent = MyAgent()
my_agent = load('MyAgent_3000')
 
my_agent.learning = False
 
start(player_x=my_agent)




#Het valideren, het plotten van een grafiek
winners = defaultdict(int)  # Dit is een mapje waar in het begin altijd nullen in zitten.
validation_agent = RandomAgent()
for i in range(100):
    winner = start(player_x=my_agent, player_o=validation_agent, ui=HEADLESS)
    winners[winner] += 1
winners[PLAYER_X] = winners[PLAYER_X] / 100
winners[PLAYER_O] = winners[PLAYER_O] / 100
winners[None] = winners[None] / 100


# wat het menu moet zijn
def main ():
  print("Kies je spel")
  print()

  choice = input("""
                    A: Tegen een ander speler
                    B: Makkelijk spel
                    C: Moeilijk spel
                    D: Plot de grafiek
                    E: Train de tegenstander
                   
                   
                    Maak een keuze: """)
  if choice == "A" or choice == "a":
    AnderSpeler()
  elif choice == "B" or choice == "b":
    MakkelijkSpel()
  elif choice == "C" or choice == "c":
    MoelijkSpel()
  elif choice == "D" or choice == "d":
    Grafiek()
  elif choice == "E" or choice == "e":
    TrainOnly()
  else:
    print("kies tussen A, B, C of D")
    print("probeer opnieuw")
    main()


# de functies van de soorten spel
def MakkelijkSpel():
   random_agent = RandomAgent()

def AnderSpeler():
  winner=start()
  if main():

def Grafiek():

def TrainOnly():

def MoeilijkSpel():