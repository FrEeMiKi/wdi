from random import randint
from itertools import product

def matrix():  # Function for generating a matrix
    while True:
        try:
            n = int(input("Columns: "))
            m = int(input("Rows: "))
            if not 0 < n < 100 or not 0 < m < 100:
                print("Size must be higher than 0 and lower than 100")
                raise ValueError
            break
        except ValueError:
            pass
    result = [[randint(0, 9) for _ in range(n)] for _ in range(m)]
    return result

matrixA = matrix()
matrixB = matrix()

print("Matrix A")
for row in matrixA:
    print(row)

print("Matrix B")
for row in matrixB:
    print(row)

def generate(y, x):
    resultrows = []
    for k in range(y):
        for z in range(2 ** x):
            combination = bin(z)[2:].zfill(x)
            new_row = [matrixA[k][j] if combination[j] == '0' else matrixB[k][j] for j in range(len(combination))]
            resultrows.append(new_row)

    part_size = len(resultrows) // y
    resultlist = [resultrows[i * part_size: (i + 1) * part_size] for i in range(y)]
    result = list(product(*resultlist))

    return result

for i in range(min(len(matrixA), len(matrixB))):
    for j in range(min(len(matrixA[0]), len(matrixB[0]))):
        print(f"\nCombinations for ({i + 1}, {j + 1}):")
        combinations = generate(i + 1, j + 1)
        for combination in combinations:
            for row in combination:
                print(row)
            print()

number_of_combinations = 0
for i in range(min(len(matrixA), len(matrixB))+1):
    for j in range(min(len(matrixA[0]), len(matrixB[0]))+1):
        number_of_combinations = number_of_combinations + 2**(i*j)

print("Ilość kombinacji to: ", number_of_combinations)