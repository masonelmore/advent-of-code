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
    for player_a, desired_outcome in plays(data):
        if desired_outcome == 'loss':
            player_b = winning_shape[player_a]
        elif desired_outcome == 'draw':
            player_b = player_a
        else:
            player_b = [a for a, b in winning_shape.items() if b == player_a][0]

        total_score += shape_score[player_b] + outcome_score[desired_outcome]

    return total_score


def plays(data):
    outcome_translation = {
        'X': 'loss',
        'Y': 'draw',
        'Z': 'win',
    }

    for line in data:
        player_a, outcome = line.strip().split(' ')
        outcome = outcome_translation[outcome]
        yield player_a, outcome


if __name__ == '__main__':
    main()
