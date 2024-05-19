import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt


def f(x):
	return x ** 2


a = 0
b = 2


def monte_carlo_integration(f, a, b, N=100000):
	x_rand = np.random.uniform(a, b, N)
	y_rand = np.random.uniform(0, f(b), N)

	count_under_curve = np.sum(y_rand <= f(x_rand))

	area_rectangle = (b - a) * f(b)
	area_under_curve = area_rectangle * count_under_curve / N

	return area_under_curve


exact_integral, error = spi.quad(f, a, b)

monte_carlo_result = monte_carlo_integration(f, a, b)
monte_carlo_error = abs(exact_integral - monte_carlo_result)

# Порівняння результатів
print(f"Точне значення інтеграла: {exact_integral} (оцінка абсолютної помилки: {error})")
print(f"Метод Монте-Карло: {monte_carlo_result} (оцінка абсолютної помилки: {monte_carlo_error})")

if np.isclose(exact_integral, monte_carlo_result, atol=1e-3):
	conclusion = "Результат методу Монте-Карло близький до точного значення інтеграла."
else:
	conclusion = "Результат методу Монте-Карло відрізняється від точного значення інтеграла."

print(conclusion)

x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title(f'Графік інтегрування f(x) = x^2 від {a} до {b}')
plt.grid()
plt.show()
