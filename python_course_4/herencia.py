class PartyAnimal:
    """
    New class for example of a instance
    """
    x = 0
    name = ""

    def __init__(self, z):
        self.name = z
        print(self.name, "Constructed")
    
    def party(self):
        self.x += 1
        print(self.name, "Party count", self.x) 

class FootballFan(PartyAnimal):
    """
    Example of inheritance
    """
    points = 0
    def touchdown(self):
        self.points += 7
        self.party()
        print(self.name,"Points", self.points)

s = PartyAnimal("sally")
s.party()

j = FootballFan("Jack")
j.party()
j.touchdown()