def solve_part1(data):
    schematic = Schematic.load(data)
    return sum(schematic.part_numbers())


def solve_part2(data):
    return -1


class Schematic:
    def __init__(self, data, width):
        self.data = data
        self.width = width

    @classmethod
    def load(cls, data):
        line = next(data)
        chars = line
        width = len(line)
        for line in data:
            chars += line
        schematic = cls(chars, width)
        return schematic

    @property
    def height(self):
        return int(len(self.data) / self.width)

    def coordinates(self, index):
        x = index % self.width
        y = int(index / self.width)
        return x, y

    def index_of(self, x, y):
        return y * self.width + x

    def char_at(self, x, y):
        return self.data[self.index_of(x, y)]

    def part_numbers(self):
        """Find all part numbers in the schematic.

        First, look for regions that are all digits. Once a region of digits is
        found, look for an adjacent symbol to determine if it's a part number.
        """
        for y in range(self.height):
            start_x = -1
            for x in range(self.width):
                char = self.char_at(x, y)

                if start_x < 0 and char.isdigit():
                    start_x = x

                end_of_line = x == self.width - 1
                end_of_number = not char.isdigit()
                if start_x >= 0 and (end_of_number or end_of_line):
                    end_x = x - 1 if end_of_number else x
                    if self.symbol_nearby(start_x, end_x, y):
                        start = self.index_of(start_x, y)
                        end = self.index_of(end_x, y)
                        part_number = self.data[start:end + 1]
                        yield int(part_number)
                    start_x = -1

    def symbol_nearby(self, start_x, end_x, start_y):
        """Check all coordinates surrounding a number for a symbol."""
        for y in range(start_y - 1, start_y + 2):
            # out of bounds
            if y < 0 or y >= self.height:
                continue
            for x in range(start_x - 1, end_x + 2):
                # out of bounds
                if x < 0 or x >= self.width:
                    continue
                # same coordinates as the number
                if start_x <= x <= end_x and y == start_y:
                    continue
                if self.is_symbol(x, y):
                    return True
        return False

    def is_symbol(self, x, y):
        char = self.char_at(x, y)
        return not char.isalnum() and char != '.'

    def show_number(self, x1, x2, y):
        """Print characters around a number to help with debugging."""
        for y in range(y - 1, y + 2):
            if y < 0 or y >= self.height:
                continue
            for x in range(x1 - 1, x2 + 2):
                if x < 0 or x >= self.width:
                    continue
                print(self.char_at(x, y), end='')
            print()
