import random

from bke import start, load, MLAgent, is_winner, opponent, train, save, RandomAgent, train_and_plot

class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward
   

def main ():
  print()
  print('Welkom bij Boter Kaas & Eieren 2.0....')
  print("Kies je spel!")
  choice = input("""
                    A: Tegen een andere speler
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
    MoeilijkSpel()
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
   start(player_o=random_agent)

def AnderSpeler():
  start()

def Grafiek(): 
 random.seed(1)
 
 my_agent = MyAgent()
 random_agent = RandomAgent()
 my_agent = MyAgent(alpha=0.8, epsilon=0.2)
 
 train_and_plot(
    agent=my_agent,
    validation_agent=random_agent,
    iterations=50,
    trainings=100,
    validations=1000)

def TrainOnly():
  my_agent = MyAgent()
 
  train(my_agent, 3000)
 
  save(my_agent, 'MyAgent_3000')
  start(player_x=my_agent)

def MoeilijkSpel():
  my_agent = load('MyAgent_3000')
 
  my_agent.learning = False
 
  start(player_x=my_agent)

main()

# opnieuw beginnen werkt niet?
# E: train de tegenstander werkt ook niet