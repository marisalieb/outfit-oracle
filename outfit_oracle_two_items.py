import random

"""
this version can group TWO items together based on the rules defined in the README (see for complete rules)

"""


class ColourWheel:
    def __init__(self):
        self.primary_colours = ['red', 'blue', 'yellow']
        self.secondary_colours = ['orange', 'green', 'purple']
        self.neutral_colours = ['white', 'black']

        self.colour_relationships = {
            'red': self.primary_colours,
            'blue': self.primary_colours,
            'yellow': self.primary_colours,
            'orange': self.neutral_colours + self.secondary_colours,
            'green': self.neutral_colours + self.secondary_colours,
            'purple': self.neutral_colours + self.secondary_colours,
            'white': self.neutral_colours + self.secondary_colours,
            'black': self.neutral_colours + self.secondary_colours
        }

    def are_colours_compatible(self, colour1, colour2):
        if colour1 == colour2:
            return True

        if colour2 in self.colour_relationships[colour1]:
            return True

        return False


class Closet:
    ALLOWED_TYPES = ['upper garment', 'lower garment']
    ALLOWED_FITS = ['loose', 'fitted']
    ALLOWED_COLOURS = None

    @classmethod
    def initialize_allowed_colours(cls, colour_wheel):

        cls.ALLOWED_COLOURS = (
            colour_wheel.primary_colours +
            colour_wheel.secondary_colours +
            colour_wheel.neutral_colours
        )

    def __init__(self, type, fit, colour, colour_wheel):

        self.type = type
        self.fit = fit
        self.colour = colour
        self.colour_wheel = colour_wheel

    def set_attributes(self, type, fit, colour, colour_wheel):

        self.type = type
        self.fit = fit
        self.colour = colour
        self.colour_wheel = colour_wheel

    def __repr__(self):
        return f"{self.fit}, {self.colour} {self.type}"

    def is_compatible(self, other):

        if self.type != other.type and self.fit != other.fit:
            #  colour compatibility
            if self.colour_wheel.are_colours_compatible(self.colour, other.colour):
                return True

        return False


colour_wheel = ColourWheel()
Closet.initialize_allowed_colours(colour_wheel)


def create_random_instance():
    type = random.choice(Closet.ALLOWED_TYPES)
    fit = random.choice(Closet.ALLOWED_FITS)
    colour = random.choice(Closet.ALLOWED_COLOURS)
    return Closet(type, fit, colour, colour_wheel)


items = [create_random_instance() for _ in range(10)]


def test_compatibility(items):
    results = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i].is_compatible(items[j]):
                results.append((i, j))
    return results


# display items
for idx, item in enumerate(items):
    print(f'Item {idx+1}: {item.fit}, {item.colour} {
          item.type}')

# test compatibility between items
compatible_pairs = test_compatibility(items)
print("\nCompatible Pairs:")
for pair in compatible_pairs:
    print(f"Item {pair[0]+1} and Item {pair[1]+1} are compatible.")
