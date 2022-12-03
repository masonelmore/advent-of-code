def main():
    input_data = load_input('dayXX_input.txt')
    solution = solve(input_data)
    print(solution)


def load_input(filename):
    with open(filename) as f:
        return f.readlines()


def solve(data):
    return True


if __name__ == '__main__':
    main()
