#Define the base class player
class Player:
  def play(self):
    print("The player is playing cricket.")
   
#Define the derived class Batsman
class Batsman(Player):
  def play(self):
    print("The bowler is batting.")
    
#Define the derived class Bowler
class Bowler(Player ):
  def play(self):
    print("The bowler is bowling.")
   
#Create objects of Batsman and Bowler
class className:
   
   def __init__(self):
      pass


batsman=Batsman()
bowler=Bowler()

#Call the play()method for each object
batsman.play()
bowler.play()