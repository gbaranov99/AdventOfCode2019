'''
Thought process:
I will create a class that has suborbital planets / children, and a parent class, as well as a depth number
Planets can be stored in a dictionary, to keep track of all the ones that exist
The first planet being the root of the tree of planets
When all planets are stored, I will do a search through all planets (loop through dictionary) and calculate total orbital number

I messed up in my interpreation of the question
Apparently children do matter, because any node that previously did not have a parent can get a new parent
Which increments all of the children of the current node appropriate to how much the new parent node orbital is
'''

class Planet:
    def __init__(self, children, height):
        self.children = children
        self.height = height

def fix_children_heights( name, height ):
    #print('wowzers')
    #print(name)
    for child in Planets[name].children:
        #print(child)
        #print(Planets[child].children)
        fix_children_heights(child, height + 1)
    Planets[name].height = height

file = open('input.txt', 'r')

Planets = {}
#root_planet = None
#root_planet = inputs[0]

for line in file:
    # Removes newline characters
    line = line.strip()
    inputs = line.split(')')
    
    # Planets with no parents yet
    if inputs[0] not in Planets:
        Planets[inputs[0]] = Planet([inputs[1],], 0)
    else:
        if inputs[1] not in Planets:
            Planets[inputs[1]] = Planet([], 0)
        Planets[inputs[1]].height = Planets[inputs[0]].height + 1
        Planets[inputs[0]].children.append(inputs[1])
        fix_children_heights(inputs[1], Planets[inputs[1]].height + 1)

    if inputs[1] not in Planets:
        Planets[inputs[1]] = Planet([], Planets[inputs[0]].height + 1)

    #print(inputs[0])
    #print(Planets[inputs[0]].children)
    #print(Planets[inputs[0]].height)

    '''
    Planets[inputs[1]].parent = inputs[0]
    Planets[inputs[0]].children.append(inputs[1])
    Planets[inputs[1]].orbit_num = Planets[inputs[0]].orbit_num + 1
    print(inputs[0])
    print(Planets[inputs[0]].children)
    print(inputs[1])
    print(Planets[inputs[1]].children)
    fix_children_heights(inputs[1], Planets[inputs[1]].orbit_num)

    else:
        Planets[inputs[1]].parent = Planets[inputs[0]]
        Planets[inputs[1]].orbit_num = Planets[inputs[0]].orbit_num + 1
        Planets[inputs[0]].children.append(inputs[1])
        fix_children_heights(inputs[1], Planets[inputs[1]].orbit_num)

    # For rest of planets
    if inputs[1] not in Planets:
        Planets[inputs[1]] = Planet()
        Planets[inputs[1]].parent = inputs[0]
        Planets[inputs[0]].children.append(inputs[1])
        Planets[inputs[1]].orbit_num = Planets[inputs[0]].orbit_num + 1
    '''


total_orbitals = 0

for planet in Planets:
    #print(planet)
    #print(Planets[planet].orbit_num)
    total_orbitals += Planets[planet].height

print(total_orbitals)
