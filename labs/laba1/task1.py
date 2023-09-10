import random

def realization_of_random(probability, m):
    """
    Генерує послідовність дискретної випадкової величини.

    param probability: Імовірність для кожного значення (список).
    param m: Кількість реалізацій.

    return: Кортеж який містить:
    1.)Послідовність реалізацій.
    2.)Кількість здійснених реалізацій.
    3.)Кількість нездійснених реалізацій.
    """

    # Ініціалізуємо порожній список для збереження реалізацій
    realizations_seq = []
    happened = 0
    not_happened = 0

    # Генеруємо послідовність
    for _ in range(m):
        # Генеруємо випадкове число від 0 до 1
        random_number = random.random()

        if random_number <= probability:
            realizations_seq.append(1)
            happened += 1
        else:
            realizations_seq.append(0)
            not_happened += 1

    return realizations_seq, happened, not_happened

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

    return realizations, dict_of_realizations


if __name__ == '__main__':
    print("Завдання №1")

    task1 = realization_of_random(probability=0.7, m=100)
    seq1 = task1[0]
    print(f'Співвідношення здійснених реалізацій до нездійсненої: {task1[1]} / {task1[2]}')
    print('Послідвоність реалізацій: ', seq1, sep='\n')

    print("\nЗавдання №2\n")

    # Параметри випадкової величини
    values = [1, 2, 3, 4]
    probability = [0.25, 0.25, 0.25, 0.25]
    M = 100

    # Генеруємо послідовність
    task2 = discrete_random_sequence(values, probability, M)
    seq2 = task2[0]
    dict2 = task2[1]

    # Результат - список реалізацій
    print('Послідвоність реалізацій: ', seq2, sep='\n')
    print('Cловник з кількістю здійснених реалізацій. реалізацій: ', dict2, sep='\n')