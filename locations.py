# Locations

class Location:
    loadlist = []

    def __init__(self, name):
        self.name = name
        Title.loadlist.append(self)
    
    def __repr__(self):
        return f"{self.name}"