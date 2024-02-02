##### MAIN FUNCTION, WHERE EVERYTHING RUNS #####

# IMPORTS
from champions import *
from fighting import *

##### TESTING AREA #####

guy = loadCharacter(path_champion_list, 'Noot Noot')
guy.curhp -= 50
print(guy.maxhp, guy.curhp)