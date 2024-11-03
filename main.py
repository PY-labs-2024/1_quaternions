import numpy as np
import quaternion
import math


class Quaternion:
    def __init__(self, w, x, y, z):
        self.w = w
        self.x = x
        self.y = y
        self.z = z

    # операция сложения кватернионов
    def __add__(self, other):
        return Quaternion(
            self.w + other.w,
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    # операция разности кватернионов
    def __sub__(self, other):
        return Quaternion(
            self.w - other.w,
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )

    # операция умножения кватернионов
    def __mul__(self, other):
        w = self.w * other.w - self.x * other.x - self.y * other.y - self.z * other.z
        x = self.w * other.x + self.x * other.w + self.y * other.z - self.z * other.y
        y = self.w * other.y - self.x * other.z + self.y * other.w + self.z * other.x
        z = self.w * other.z + self.x * other.y - self.y * other.x + self.z * other.w
        return Quaternion(w, x, y, z)

    # комплексно-сопряженный кватернион
    def conjugate(self):
        return Quaternion(self.w, -self.x, -self.y, -self.z)

    # норма кватерниона
    def norm(self):
        return math.sqrt(self.w**2 + self.x**2 + self.y**2 + self.z**2)

    # обратный кватернион
    def inverse(self):
        conj = self.conjugate()
        norm_sq = self.norm()**2
        return Quaternion(conj.w / norm_sq, conj.x / norm_sq,
                          conj.y / norm_sq, conj.z / norm_sq)

    # поворот вектора с нулевой действительной частью в соответствии с кватернионом
    def rotate_vector(self, vector):
        vector_quat = Quaternion(0, *vector)
        rotated_vector = self * vector_quat * self.inverse()
        return (round(rotated_vector.x,8), round(rotated_vector.y,8), round(rotated_vector.z,8))

    def __str__(self):
        return f"Кватернион({self.w}, {self.x}, {self.y}, {self.z})"


# Пример использования
q1 = Quaternion(1, 0, 1, 2)
q2 = Quaternion(1, 1, 2, 0)

q11 = np.quaternion(1, 0, 1, 2)
q22 = np.quaternion(1, 1, 2, 0)

# Сложение
print(f"Сложение {q1} и {q2}:\n\nРезультат для реализации класса: {q1 + q2}")
print(f"Результат для библиотеки quaternion: {q11 + q22}\n")

# Умножение
print(f"Умножение {q1} и {q2}:\n\nРезультат для реализации класса: {q1 * q2}")
print(f"Результат для библиотеки quaternion: {q11 * q22}\n")

# Вращение вектора
vector = (1, 0, 0) # вектор с нулевой действительной частью
rotated_vector = q1.rotate_vector(vector)
print(f"Вращение вектора {vector}:\n\nРезультат для реализации класса: {rotated_vector}")
print(f"Результат для библиотеки quaternion: {quaternion.rotate_vectors(q11, vector)}\n")
