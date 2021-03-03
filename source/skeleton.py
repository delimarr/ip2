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
        self.visits += 1
        
class Map:
    def __init__(self):
        self.id = 'mapExample' 
        self.nodes = []
        self.edges = []

    # POST: -
    # PAST: -
    def initMap(self):
        #TODO: create node and edge objects according to map difficulty and matrice
        #Fill tuples of all objects -> NodeObject.edges(), EdgeObject.nodes()
        #NodeObject.edges() Contains all edges which are connected to a node
        #EdgeObject.nodes() Contains all nodes which are connected to a edge (always 2)
        #Fill MapObject.nodes[] and MapObject.edges[] -> Those contain all active nodes and edges for a map
        return

    # POST: takes current as float
    # PAST: returns the node object according to the current
    def getPosition(self, current):
        #TODO: take current values of map.py matrices in main branch (main diagonal matches value of each node (x=2, y=2 -> current value of node 3 etc.))
        return #NodeObject

        
class Player:
    def __init__(self):
        self.name = "Player1"
        self.score = 0
        self.position = None 
        self.map = None #matrice
        self.path = [] #contains all visited edges

    def makeMap(self):
        self.map = Map()
        self.id = getMap()
        self.map.initMap() 
        return

    # POST: -
    # PAST: -
    def setName(self):
        #TODO: read player name over stdin and change variable
        return

    def initGame(self):
        self.setName()
        self.makeMap()
        return

    # POST: takes newPosition as a node object
    # PAST: returns edge object which connects the old and the new position of the player
    def getEdge(self, newPosition):
        #TODO:
        return #edgeObject

    # POST: -
    # PAST: -
    def setScore(self):
        #TODO: calculates the score from path the player walked 
        return

    # POST: tbd
    # PAST: tbd
    def publicScore(self):
        #TODO: tbd
        return 

    # POST: Takes a new position as a nodeObject
    # PAST: Returns if the two nodes (old position and new position of player) are actually connected and no error was made while detecting
    def isNewPosValid(self, newPosition):
        return #boolean 

    # POST: -
    # PAST: -
    def step(self):
        #TODO: Move player from old node to new node and update player information
        return

    # POST: -
    # PAST: Returns True or False according to the game state
    def isGameFinished(self):
        return #boolean


# POST: takes INA-object
# PAST: return the highest current (mA) from this measurement as float .1f
def getCurrent(ina):
    #TODO: return the current 
    return

# POST: String of map difficulty
# PAST: Returns the matrice according to difficulty
def getMap(self, difficulty):
    return #

# POST: tbd
# PAST: tbd
def quit():
    #TODO: tbd
    return

# POST: tbd
# PAST: tbd
def restart():
    #TODO: tbd
    return
    
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