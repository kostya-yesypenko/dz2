import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, simplify

# Задані точки для інтерполяції
xi = np.array([-4, -2, 0, 3])
yi = np.array([-18, 8, -6, 3])

# Точки, у яких потрібно знайти значення функції
points_to_interpolate = [-3.5, -3, -0.5, 2]
# Створення символьних змінних для використання у формулі
x = symbols('x')

# Обчислення інтерполяційного многочлена Лагранжа
def lagrange_poly(x, xi, yi):
    n = len(xi)
    result = 0
    for j in range(n):
        term = yi[j]
        for i in range(n):
            if i != j:
                term *= (x - xi[i]) / (xi[j] - xi[i])
        result += term
    return simplify(result)

# Виведення формули многочлена Лагранжа
print("Формула многочлена Лагранжа:")
lagrange_formula = lagrange_poly(x, xi, yi)
print(lagrange_formula)


# Вивід коефіцієнтів многочлена
print("Інтерполяційний многочлен Лагранжа:")
print(lagrange_poly(np.array(points_to_interpolate), xi, yi))

# Обчислення значень функції в заданих точках
print("Значення функції в заданих точках:")
for point in points_to_interpolate:
    print(f"f({point}) = {lagrange_poly(point, xi, yi)}")

# Побудова графіка інтерполяційної функції
x_values = np.linspace(-4, 3, 100)
y_values = lagrange_poly(x_values, xi, yi)

plt.plot(x_values, y_values, label='Interpolation')
plt.title('Interpolation Graph')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
