from ina219 import INA219 
from map import *
from led import *

class Node:
    def __init__(self):
        self.id = 'n#'
        self.edges = None #tuple of all edges, which are connected to this node
        self.maxCurrent = 100.0 #in mA

class Edge:
    def __init__(self):
        self.id = 'e#'
        self.nodes = None #tuple of the two according nodes
        self.length = 0
        self.visits = 0

    def incrementVisits(self):
        self.visits =+ 1
        
class Map:
    def __init__(self):
        self.id = 'mapExample' 

    def initMap(self):
        #make Nodes and Edges from the map and set their attributes
        return

    def getPosition(self, ina):
        #measures the current and gives the appropriate position back$
        #ina.current()
        return "Node"


class Player:
    def __init__(self):
        self.name = "Player1"
        self.score = 0
        self.position = 0
        self.map = 'map'
        self.path = []

    def setScore(self):
        #calculates and sets the score
        return

    def publicScore(self):
        #send Score and Playername to the FHNW Dashboard 
        return

    def setName(self):
        #prompt PlayerName and set
        return

    def getEdge(self, newPosition):
        #returns the edge, which connects the old position with the new position
       return "edge" 
    
    def initGame(self):
        self.setName()
        self.makeMap()
        return

    def makeMap(self):
        self.map = Map()
        self.id = getMap()
        self.map.initMap() 
        return

    def isGameFinished(self):
        return False

    def step(self):
        #move the player from nodeA to nodeB and update player
        return

    def isNewPosValid(self, newPosition):
        #returns true if the newPosition is a valid move from the current Position
        return True


def getMap():
    #prompt difficulty and returns the specific map
    return

def restart():
    return;

def run(ina, led):
    player = Player()
    player.initGame()

    while player.isGameFinished():
        newPosition = player.map.getPosition(ina)
        if player.isNewPosValid(newPosition):
            player.step(newPosition)
            led.lightMap(player)

    player.setScore()
    player.publicScore()
        
def main():
    SHUNTOHMS = 0.1
    ina = INA219(SHUNTOHMS)
    ina.configure()

    led = Led()
    led.configure()

    while True:
        if restart():
            run(ina, led)
        elif exit():
            break


if __name__=="__main__":
    main()
