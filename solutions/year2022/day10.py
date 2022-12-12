def solve_part1(data):
    handler = sample_signal_strength(start=20, period=40)
    strength = run_program(data, handler)
    return strength


def solve_part2(data, draw=True):
    handler = decode_image(buffer_width=40)
    image_buffer = run_program(data, handler)
    if draw:
        draw_buffer(image_buffer)
    return image_buffer


def run_program(data, handler):
    cycles = 0
    register = 1
    for instruction, arg in parse_instructions(data):
        for _ in range(instruction_cycles(instruction)):
            handler(cycles, register)
            cycles += 1
        if instruction == 'addx':
            register += arg
    # bug in decode_image requires a final call to save the last to the buffer
    return handler(cycles, register)


def parse_instructions(data):
    for line in data:
        parts = line.split(' ')
        if len(parts) == 1:
            instruction, arg = parts[0], None
        else:
            instruction, arg = parts[0], int(parts[1])
        yield instruction, arg


def instruction_cycles(instruction):
    if instruction == 'noop':
        return 1
    elif instruction == 'addx':
        return 2
    else:
        raise ValueError('invalid instruction:', instruction)


def sample_signal_strength(start, period):
    strength = 0
    next_sample = start

    def handler(cycles, register):
        nonlocal strength, next_sample
        cycles += 1  # off-by-one hack for part2
        if cycles == next_sample:
            strength += cycles * register
            next_sample += period
        return strength

    return handler


def decode_image(buffer_width):
    buffer = []
    line = ''

    def handler(cycles, register):
        nonlocal buffer_width, buffer, line
        x = cycles % buffer_width
        if x == 0 and cycles > 0 or cycles == 240:  # eh, it works
            buffer.append(line)
            line = ''
        if x - 1 == register or x == register or x + 1 == register:
            line += '#'
        else:
            line += '.'
        return buffer

    return handler


def draw_buffer(buffer):
    for line in buffer:
        print(line)
