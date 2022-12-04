def gen(items):
    for item in items:
        yield item


def load_input(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()
