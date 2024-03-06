def forward_elimination(A, b):
    n = len(A)
    for i in range(n):
        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]

def backward_substitution(A, b):
    n = len(A)
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = b[i]
        for j in range(i+1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]
    return x

def gauss_seidel_normalize(A, b):
    n = len(A)
    for i in range(n):
        pivot = A[i][i]
        for j in range(n):
            A[i][j] /= pivot
        b[i] /= pivot


def gauss_seidel(A, b, x0, tolerance=0.001, max_iterations=100):
    gauss_seidel_normalize(A, b)
    forward_elimination(A, b)

    # Початкове наближення
    x = x0.copy()

    # Зберігатимемо наближені значення після кожної ітерації
    iterations = [x.copy()]

    # Похибка
    errors = []

    for _ in range(max_iterations):
        x_old = x.copy()
        for i in range(len(A)):
            sigma = sum(A[i][j] * x[j] for j in range(len(A))) - A[i][i] * x[i]
            x[i] = (b[i] - sigma) / A[i][i]
        iterations.append(x.copy())

        # Обчислення похибки
        error = max(abs(x[i] - x_old[i]) for i in range(len(x)))
        errors.append(error)

        # Перевірка на збіжність
        if error < tolerance:
            break

    return iterations, errors


# Приклад використання:
A = [[4, -5, 40, 0],
     [10, -4, 0, 50],
     [32, 0, 4, -4],
     [0, 32, 0, -9]]
b = [19, 0, 34, -49]
x0 = [0] * len(b)

print("Система рівнянь:")
for i in range(len(A)):
    row = " ".join(f"{A[i][j]}x{j + 1}" for j in range(len(A[i])))
    print(f"{row} = {b[i]}")

print("\nРозв'язок методом Гауса-Зейделя:")
iterations, errors = gauss_seidel(A, b, x0)

# Виведення наближених значень після кожної ітерації та значення похибки
print("\nНаближені значення після кожної ітерації:")
iteration_number = 1
for iteration, error in zip(iterations, errors):
    print(f"Iteration {iteration_number}: {iteration}, Похибка: {error}")
    iteration_number += 1



print("\nРозв'язок системи:", iterations[-1])


