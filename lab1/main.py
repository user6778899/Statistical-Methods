import numpy as np
import matplotlib.pyplot as plt


a = 1
n_points = 100000

# Генерация случайных точек в квадрате [-a, a] x [-a, a]
rng = np.random.default_rng()
points = rng.uniform(-a, a, size=(n_points, 2))

# Проверка принадлежности кругу
r_values = [1.0, 0.5, 1/3, 0.25, 0.2]
for r in r_values:
    in_circle = np.sum(points[:, 0]**2 + points[:, 1]**2 <= r**2)
    p_hat = in_circle / n_points
    print(f"r = {r:.3f}, p_hat = {p_hat:.5f}, p = {np.pi * r**2 / 4}")
