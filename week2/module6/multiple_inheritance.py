class family:
    def __init__(self, address):
        self.address = address

    
class school:
    def __init__(self, id, lvl):
        self.id = id
        self.lvl = lvl


class sports:
    def __init__(self, game):
        self.game = game



class student(family, school, sports):
    def __init__(self, name, address, id, lvl, game):
        self.name = name
        family.__init__(self, address)
        school.__init__(self, id, lvl)
        sports.__init__(self, game)

    def __repr__(self):
        return f'''Name: {self.name}
ID: {self.id}
Class: {self.lvl}
Address: {self.address}
Game: {self.game}
'''
        
mahir = student("Mahir", "Dhaka", 23, 5, "Football")


print(mahir)