import random
import matplotlib.pyplot as plt

if __name__ == '__main__':
    print('Лабораторна робота №2', 'Варіант - 11')

    M = 100

    lower_bound = 1
    upper_bound = 2

    realizations = []

    for _ in range(M):
        realization = random.uniform(lower_bound, upper_bound)
        realizations.append(realization)

    # Виводимо список реалізацій
    print(realizations)

    num_bins = 10  # Можете змінити кількість бінів на свій смак

    # Побудова гістограми
    plt.hist(realizations, bins=num_bins, color='blue', alpha=0.7)
    plt.xlabel('Значення')
    plt.ylabel('Частота')
    plt.title('Гістограма неперервної випадкової величини')
    plt.grid(True)

    # Відображення графіка
    plt.show()