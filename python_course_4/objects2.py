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
    
s = PartyAnimal("Jack")
s.party()

j = PartyAnimal("Noe")
j.party()
s.party()