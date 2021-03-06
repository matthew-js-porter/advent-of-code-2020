def calculate(expenses: list, magic_number: int) -> int:
    for i, first in enumerate(expenses):
        for j, second in enumerate(expenses[i + 1:]):
            for third in expenses[j + 1:]:
                if first + second + third == magic_number:
                    return first * second * third


if __name__ == '__main__':
    with open('input.txt') as data:
        expenses = [int(expense) for expense in data.read().splitlines()]
        print(calculate(expenses, 2020))
