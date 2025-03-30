import numpy as np
import matplotlib.pyplot as plt

# Параметры
a = 1
r_values = [1.0, 0.5, 1/3, 0.25, 0.2]
n_max = 10000
epsilon_targets = [1e-1, 1e-2, 1e-3, 1e-4]

# Генерация точек и расчет p_hat
rng = np.random.default_rng()
n_values = np.arange(1, n_max + 1, 100)

for r in r_values:
    p_true = np.pi * r**2 / 4
    p_hat_values = []
    epsilon_values = []
    
    for n in n_values:
        points = rng.uniform(-a, a, size=(n, 2))
        in_circle = np.sum(points[:, 0]**2 + points[:, 1]**2 <= r**2)
        p_hat = in_circle / n
        p_hat_values.append(p_hat)
        epsilon_values.append(abs(p_hat - p_true))
    
    # График p_hat(n)
    plt.figure()
    plt.plot(n_values, p_hat_values, label='$\hat{p}(n)$')
    plt.axhline(y=p_true, color='r', linestyle='--', label='$p$')
    plt.xlabel('Количество точек, $n$')
    plt.ylabel('$\hat{p}$')
    plt.legend()
    plt.title(f'Оценка вероятности для $r = {r}$')
    plt.grid(True)
    plt.show()
    
    # График epsilon(n)
    plt.figure()
    plt.plot(n_values, epsilon_values, label='$\epsilon(n)$')
    plt.xlabel('Количество точек, $n$')
    plt.ylabel('$\epsilon$')
    plt.legend()
    plt.title(f'Ошибка оценки для $r = {r}$')
    plt.grid(True)
    plt.show()

# Расчет N(epsilon)
N_results = {r: [] for r in r_values}

for r in r_values:
    p_true = np.pi * r**2 / 4
    for epsilon in epsilon_targets:
        n = 1
        while True:
            points = rng.uniform(-a, a, size=(n, 2))
            in_circle = np.sum(points[:, 0]**2 + points[:, 1]**2 <= r**2)
            p_hat = in_circle / n
            if abs(p_hat - p_true) <= epsilon:
                N_results[r].append(n)
                break
            n += 1

# График N(epsilon)
plt.figure()
for r in r_values:
    plt.plot(epsilon_targets, N_results[r], 'o-', label=f'$r = {r}$')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Точность, $\epsilon$')
plt.ylabel('Необходимое $N$')
plt.legend()
plt.title('Зависимость $N(\epsilon)$ для разных $r$')
plt.grid(True)
plt.show()
