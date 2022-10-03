import random

from bke import start, load, MLAgent, is_winner, opponent, train, save, RandomAgent, plot_validation, validate, train_and_plot
 
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
   
 
random.seed(1)
 
my_agent = MyAgent()
random_agent = RandomAgent()
 
train_and_plot(
    agent=my_agent,
    validation_agent=random_agent,
    iterations=50,
    trainings=100,
    validations=1000)

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
 validation_agent = RandomAgent()
 
 validation_result = validate(agent_x=my_agent, agent_o=validation_agent, iterations=100)
 
 plot_validation(validation_result)
def TrainOnly():
  my_agent = MyAgent()
 
  train(my_agent, 3000)
 
  save(my_agent, 'MyAgent_3000')

def MoeilijkSpel():
  my_agent = load('MyAgent_3000')
 
  my_agent.learning = False
 
  start(player_x=my_agent)




# #Het valideren, het plotten van een grafiek
# winners = defaultdict(int)  # Dit is een mapje waar in het begin altijd nullen in zitten.
# validation_agent = RandomAgent()
# for i in range(100):
#     winner = start(player_x=my_agent, player_o=validation_agent, ui=HEADLESS)
#     winners[winner] += 1
# winners[PLAYER_X] = winners[PLAYER_X] / 100
# winners[PLAYER_O] = winners[PLAYER_O] / 100
# winners[None] = winners[None] / 100

  