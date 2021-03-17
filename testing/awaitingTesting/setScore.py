# author: Anja
# General conventions:
#       - functions, variables: firstLetterLowerCase
#       - class: FirstLetterCapital
#       - constant: CAPITAL
#############################################################################

'''
Doc: your remarks, ideas
'''

# POST: -
# PAST: -

def setScore(self):
    #TODO: calculates the score from path the player walked 

    for edge in self.path:
        self.score += edge.length