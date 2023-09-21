import random
import matplotlib.pyplot as plt

if __name__ == '__main__':
    print('Лабораторна робота №2', 'Варіант - 11')

    M = 500

    a = 1
    b = 2

    realizations = []

    for _ in range(M):
        r = random.uniform(a, b)
        f = (b - a) * r + a
        realizations.append(f)

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