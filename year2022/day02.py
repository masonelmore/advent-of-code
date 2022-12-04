winning_shape = {
    'A': 'C',  # Rock beats Scissors
    'B': 'A',  # Paper beats Rock
    'C': 'B',  # Scissors beats Paper
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


def solve_part1(data):
    total_score = 0
    for player_a, player_b in next_move(data):
        if winning_shape[player_b] == player_a:
            outcome = 'win'
        elif winning_shape[player_a] == player_b:
            outcome = 'loss'
        else:
            outcome = 'draw'

        total_score += shape_score[player_b] + outcome_score[outcome]

    return total_score


def solve_part2(data):
    total_score = 0
    for player_a, outcome in desired_outcome(data):
        if outcome == 'loss':
            player_b = winning_shape[player_a]
        elif outcome == 'draw':
            player_b = player_a
        else:
            player_b = [a for a, b in winning_shape.items() if b == player_a][0]

        total_score += shape_score[player_b] + outcome_score[outcome]

    return total_score


def next_move(data):
    shape_translation = {
        'X': 'A',  # Rock
        'Y': 'B',  # Paper
        'Z': 'C',  # Scissors
    }

    for line in data:
        player_a, player_b = line.split(' ')
        player_b = shape_translation[player_b]
        yield player_a, player_b


def desired_outcome(data):
    outcome_translation = {
        'X': 'loss',
        'Y': 'draw',
        'Z': 'win',
    }

    for line in data:
        player_a, outcome = line.split(' ')
        outcome = outcome_translation[outcome]
        yield player_a, outcome
