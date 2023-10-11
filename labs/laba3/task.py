import math
import random


def calculate_x(c, mean, n):
    suma = 0
    for i in range(0, n+1):
        r = random.random()
        suma += c[i][n] * r
    return suma + mean[n]


def generate_c_matrix(k):
    n = len(k)
    c = [[0] * n for _ in range(n)]

    c[0][0] = math.sqrt(k[0][0])
    c[0][1] = k[0][1] / c[0][0]
    c[1][1] = math.sqrt(k[1][1] - math.pow(c[0][1], 2))
    c[1][0] = (k[1][0] - c[0][1] * c[0][0]) / c[1][1]

    # for i in range(n):
    #     for j in range(i + 1):
    #         suma = sum(c[l][i] * c[l][j] for l in range(i))
    #         if i == j:
    #             c[i][j] = math.sqrt(k[i][i] - suma)
    #         else:
    #             c[i][j] = (1.0 / c[j][j] * (k[i][j] - suma))
    return c


N = 10
k = [[300, 120],
     [120, 300]]
mean = [0, 0]
r0 = 10

# points = []
c = generate_c_matrix(k)
distances = []
hits = 0

print("c = ", *c, sep='\n')
print()

for i in range(N):
    x = calculate_x(c, mean, 0)
    y = calculate_x(c, mean, 1)

    print('Спроба №', i + 1)
    print('x = ', x, ', y = ', y, sep='')

    distance = math.sqrt(x ** 2 + y ** 2)
    print('Відстань від точки розриву снаряда до цілі =', distance, end=', Результат: ')
    if distance <= r0:
        hits += 1
        print('Влучив')
    else:
        print('Не влучив')
    print()
    # points.append((x, y))

# distances = [math.sqrt(x ** 2 + y ** 2) for x, y in points]

# Знаходимо кількість попадань
# hits = sum(1 for d in distances if d <= r0)

print(f"Кількість попадань: {hits}")