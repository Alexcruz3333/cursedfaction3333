class CursedFaction:
    def __init__(self, name, curse_level):
        self.name = name
        self.curse_level = curse_level

    def describe(self):
        return f"The faction '{self.name}' is cursed at level {self.curse_level}!"

    def intensify_curse(self, amount):
        self.curse_level += amount
        return f"Curse level increased to {self.curse_level}."