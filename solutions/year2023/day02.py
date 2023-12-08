import math


def solve_part1(data):
    # Find bags with no more than:
    #   12 red cubes, 13 green cubes, and 14 blue cubes.
    # Return the sum of their IDs.
    return sum(
        bag.id for bag
        in (Bag.from_line(line) for line in data)
        if bag.no_more_than(red=12, green=13, blue=14)
    )


def solve_part2(data):
    # For each game, find the minimum set of cubes that must have been present.
    # Return the sum of the power of these sets.
    return sum(
        math.prod(bag.min_required()) for bag
        in (Bag.from_line(line) for line in data)
    )


class Bag:
    """A collection of observations of cubes randomly pulled out of a bag."""

    def __init__(self, game_id):
        self.id = game_id
        self.observations = {
            'red': [],
            'blue': [],
            'green': [],
        }

    @classmethod
    def from_line(cls, line):
        # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        game_id, observations = line.split(':')
        game_id = game_id.split(' ')[-1]
        bag = Bag(int(game_id))
        for observation in observations.split(';'):
            if ',' not in observation:
                count, color = observation.strip().split(' ')
                bag.observe(count, color)
                continue
            for cube in observation.split(', '):
                count, color = cube.strip().split(' ')
                bag.observe(count, color)
        return bag

    def observe(self, count, color):
        """Write down the `count` and `color` of cubes we see."""
        self.observations[color].append(int(count))

    def max_seen(self, color):
        """The highest value of `color` we have observed."""
        return max(self.observations[color])

    def no_more_than(self, red, green, blue):
        """Check if we have observed no more than `red`, `green`, and `blue` cubes."""
        return (
                self.max_seen('red') <= red
                and self.max_seen('green') <= green
                and self.max_seen('blue') <= blue
        )

    def min_required(self):
        """Return the minimum required cubes for each color (r,g,b)."""
        return self.max_seen('red'), self.max_seen('green'), self.max_seen('blue')
