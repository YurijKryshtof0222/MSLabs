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

        sum = happened + not_happened

    return realizations_seq, happened / sum


if __name__ == '__main__':
    print('Завдання №1', 'Варіант - 11')
    print()
    m = int(input('Введіть значення M - кількість реалізацій :'))
    probability = float(input('Введіть значення P - ймовірністі [0, 1]'))

    task1 = realization_of_random(probability=probability, m=m)
    seq1 = task1[0]
    print(f'Ймовірність: {task1[1]}')
    print('Послідвоність реалізацій: ', seq1, sep='\n')
