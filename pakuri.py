class Pakuri:

    def __init__(self, species):
        self.species = species
        self.attack = (len(species) * 7) + 9

    def __lt__(self, other):
        return self.attack <= other.attack

    def get_species(self):
        return self.species