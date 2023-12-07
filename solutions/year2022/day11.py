import operator
from functools import reduce
from itertools import islice


def solve_part1(data):
    monkeys = parse_monkeys(data)
    monkey_business = monkey_around(monkeys, rounds=20)
    return monkey_business


def solve_part2(data):
    return -1
    monkeys = parse_monkeys(data)
    monkey_business = monkey_around(
        monkeys,
        rounds=10000,
        have_anxiety_meds=False,
    )
    return monkey_business


def monkey_around(monkeys, rounds, have_anxiety_meds=True):
    monkey_inspections = [0] * len(monkeys)
    for _ in range(rounds):
        for monkey in monkeys:
            while result := monkey.inspect(have_anxiety_meds):
                target_monkey, worry_level = result
                monkeys[target_monkey].catch(worry_level)
                monkey_inspections[monkey.number] += 1
    top_two = islice(sorted(monkey_inspections, reverse=True), 2)
    monkey_business = reduce(operator.mul, top_two, 1)
    return monkey_business


def parse_monkeys(data):
    monkeys = []
    # Monkey <n>:
    #   Starting items: [<n>, ...]
    #   Operation: new = old <operation>
    #   Test: divisible by <n>
    #     If true: throw to monkey <n>
    #     If false: throw to monkey <n>
    for line in data:
        if not line:
            continue

        # regex would have ben easier to read. but I'm already done...
        monkey_number = int(line.split(' ')[-1].strip(':'))
        line = next(data)
        items = line.split(':')[-1].split(',')
        items = [int(item.strip()) for item in items]
        line = next(data)
        operation = line.split(':')[-1].split('=')[-1].strip()
        line = next(data)
        test_value = int(line.split(' ')[-1])
        line = next(data)
        true_monkey = int(line.split(' ')[-1])
        line = next(data)
        false_monkey = int(line.split(' ')[-1])

        monkey = Monkey(
            number=monkey_number,
            items=items,
            operation=operation,
            test_val=test_value,
            true_dst=true_monkey,
            false_dst=false_monkey,
        )

        monkeys.append(monkey)
    return monkeys


class Monkey:
    def __init__(self, number, items, operation, test_val, true_dst, false_dst):
        self.number = number
        self._items = items
        # these dynamic functions are probably unnecessary. :shrug:
        self._test = self._make_test(test_val, true_dst, false_dst)
        self._operation = self._make_operation(operation)

    def inspect(self, anxiety_meds=True):
        if not self._items:
            return None

        worry_level = self._items.pop(0)
        worry_level = self._operation(worry_level)
        if anxiety_meds:
            worry_level //= 3  # much relief. phew!
        target_monkey = self._test(worry_level)
        return target_monkey, worry_level

    def catch(self, item):
        self._items.append(item)

    @staticmethod
    def _make_test(value, true_dst, false_dst):
        def test(worry_level):
            if worry_level % value == 0:
                return true_dst
            else:
                return false_dst

        return test

    @staticmethod
    def _make_operation(operation):
        parts = operation.split(' ')

        match parts[1:]:
            case ["+", "old"]:
                return lambda old: old + old
            case ["*", "old"]:
                return lambda old: old * old
            case ["+", n]:
                return lambda old: old + int(n)
            case ["*", n]:
                return lambda old: old * int(n)

        raise ValueError('invalid operation:', operation)
