def main():
    input_data = load_input('d02_input.txt')
    solution = solve(input_data)
    print(solution)


def load_input(filename):
    with open(filename) as f:
        return f.readlines()


def solve(data):
    winning_shape = {
        'A': 'C',   # Rock beats Scissors
        'B': 'A',   # Paper beats Rock
        'C': 'B',   # Scissors beats Paper
    }

    shape_score = {
        'A': 1,
        'B': 2,
        'C': 3,
    }

    outcome_score = {
        'loss': 0,
        'draw': 3,
        'win': 6,
    }

    total_score = 0
    for player_a, player_b in plays(data):
        if winning_shape[player_b] == player_a:
            outcome = 'win'
        elif winning_shape[player_a] == player_b:
            outcome = 'loss'
        else:
            outcome = 'draw'

        total_score += shape_score[player_b] + outcome_score[outcome]

    return total_score


def plays(data):
    shape_translation = {
        'X': 'A',   # Rock
        'Y': 'B',   # Paper
        'Z': 'C',   # Scissors
    }

    for line in data:
        player_a, player_b = line.strip().split(' ')
        player_b = shape_translation[player_b]
        yield player_a, player_b


if __name__ == '__main__':
    main()
