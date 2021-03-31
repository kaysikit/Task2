n = int(input("Введите размер матрицы: "))
matrix = [[0] * n for i in range(n)]
value = 1
coefficent = 0

matrix[n // 2][n // 2] = n * n
for el in range(n // 2):

    for i in range(n - coefficent):
        matrix[el][i + el] = value
        value += 1

    for i in range(el + 1, n - el):
        matrix[i][-el - 1] = value
        value +=1

    for i in range(el + 1, n - el):
        matrix[-el - 1][-i - 1] = value
        value +=1

    for i in range(el + 1, n - (el + 1)):
        matrix[-i - 1][el] = value
        value += 1

    coefficent += 2

for i in matrix:
    print(*i)