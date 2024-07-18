import random

"""
this version can group THREE items together based on the rules defined in the README (see for complete rules)

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

    def are_colours_compatible(self, colour1, colour2, colour3):

        if colour1 == colour2 == colour3:
            return True

        if (colour2 in self.colour_relationships[colour1] and
                colour3 in self.colour_relationships[colour1] and
                colour3 in self.colour_relationships[colour2]):
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

    def is_compatible_triples(self, other1, other2):
        items = [self, other1, other2]

        # determine types and fits
        types = [item.type for item in items]
        fits = [item.fit for item in items]
        colours = [item.colour for item in items]

        # if all items are upper or all lower, then false
        # so that a look is always at least one of each type
        if all(t == 'upper garment' for t in types) or all(t == 'lower garment' for t in types):
            return False

        # if all items have same fit, return False
        if all(f == 'loose' for f in fits) or all(f == 'fitted' for f in fits):
            return False

        # check for case where two items have same type and fit, so only third is different in both type and fit
        if (types[0] == types[1] and fits[0] == fits[1]) or \
           (types[0] == types[2] and fits[0] == fits[2]) or \
           (types[1] == types[2] and fits[1] == fits[2]):
            return False

        # check colour comp
        if self.colour_wheel.are_colours_compatible(colours[0], colours[1], colours[2]):
            return True

        return False


colour_wheel = ColourWheel()

# initialize class attribute
Closet.initialize_allowed_colours(colour_wheel)


def create_random_instance():
    type = random.choice(Closet.ALLOWED_TYPES)
    fit = random.choice(Closet.ALLOWED_FITS)
    colour = random.choice(Closet.ALLOWED_COLOURS)
    return Closet(type, fit, colour, colour_wheel)


# create  random items
items = [create_random_instance() for _ in range(10)]


def test_triple_compatibility(items):
    results = []
    n = len(items)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if items[i].is_compatible_triples(items[j], items[k]):
                    results.append((i, j, k))
    return results


# display items
for idx, item in enumerate(items):
    print(f'Item {idx+1}: {item.fit}, {item.colour} {item.type}')


#  compatibility among triples
compatible_triples = test_triple_compatibility(items)

if compatible_triples:
    print("\nCompatible Triples:")
    for triple in compatible_triples:
        print(f"Items {triple[0] + 1}, {triple[1] +
              1}, {triple[2] + 1} are compatible.")
else:
    print("\nCompatible Triples: None")
