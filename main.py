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
                    A: Train de tegenstander 
                    B: Tegen een andere speler
                    C: Makkelijk spel
                    D: Moeilijk spel
                    E: Plot de grafiek
                   
                   
                    Maak een keuze: """)
  if choice == "A" or choice == "a":
    TrainOnly()
  elif choice == "B" or choice == "b":
    AnderSpeler() 
  elif choice == "C" or choice == "c":
    MakkelijkSpel()
  elif choice == "D" or choice == "d":
    MoeilijkSpel()
  elif choice == "E" or choice == "e":
    Grafiek()

  else:
    print()
    print("Kies tussen A, B, C of D")
    print("Probeer opnieuw.....")
    main()


def again ():
  print()
  again = input("Wil je verder spelen? Ja of Nee? ")
  if again == "ja" or again == "Ja" or again == "JA":
        print(" ")
        main()
      
  else:
       print() 
       print("Tot ziens! :)")
       quit()
      
# de functies van de soorten spel
def MakkelijkSpel():
   random_agent = RandomAgent()
   start(player_o=random_agent)
   again()

def AnderSpeler():
  start()
  again()

def Grafiek(): 
 print()
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
  print()
  print("Gelukt, je hebt je tegenstander getraint.")
  again()

def MoeilijkSpel():
  my_agent = load('MyAgent_3000')
 
  my_agent.learning = False
 
  start(player_x=my_agent)
  again()


main()

