import random


def discrete_random_sequence(values, probability, m):
    """
    Генерує послідовність дискретної випадкової величини.

    param values: Список можливих значень.
    param probability: Імовірність для кожного значення (список).
    param m: Кількість реалізацій.

    return: Кортеж який містить
    1.)Послідовність реалізацій.
    2.)Словник з кількістю здійснених реалізацій.
    """
    realizations = []
    cumulative_probabilities = [sum(probability[:i + 1]) for i in range(len(probability))]
    dict_of_realizations = {value: 0 for value in values}

    for _ in range(m):
        random_number = random.random()
        realization = None

        for i, cumulative_prob in enumerate(cumulative_probabilities):
            if random_number <= cumulative_prob:
                realization = values[i]
                break

        dict_of_realizations[realization] += 1
        realizations.append(realization)

    return realizations, {k: v / 100 for k, v in dict_of_realizations.items()}


if __name__ == '__main__':
    print('Завдання №2', 'Варіант - 11')
    print()

    # Параметри випадкової величини
    # probability = [0.25, 0.25, 0.25, 0.25]
    # M = 100

    m = int(input('Введіть значення M - кількість реалізацій: '))
    value_len = int(input("Введіть кількість значень: "))
    values = [x for x in range(1, value_len + 1)]
    probability = list()
    for x in range(1, value_len + 1):
        probability.append(float(input(f'Введіть значення імовірності P для значення {x}:')))

    # Генеруємо послідовність
    task2 = discrete_random_sequence(values, probability, m)
    seq2 = task2[0]
    dict2 = task2[1]

    # Результат - список реалізацій
    print('Послідвоність реалізацій: ', seq2, sep='\n')
    print('Cловник з кількістю здійснених реалізацій: ', dict2, sep='\n')