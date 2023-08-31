import math
import random
import numpy as np

class LinearRegression:
    def __init__(self, calc_list: np.ndarray):
        self.calc_list = calc_list
        self.x_mean = np.mean(self.calc_list[:, 0])
        self.y_mean = np.mean(self.calc_list[:, 1])
        self.slope = self.calculate_slope()
        self.intercept = self.calculate_intercept()

    def calculate_standard_deviation(self, std_list):
        sum = 0.0

        for i in std_list:
            sum += i

        avg = sum / std_list.__len__()
        sum = 0.0

        for i in std_list:
            sum += (i - avg) ** 2

        return math.sqrt(sum / (std_list.__len__() - 1))

    def calculate_slope(self):
        # m = r * sy / sx

        r1 = 0
        c = 0
        d = 0

        for [x, y] in self.calc_list:
            a = (x - self.x_mean)
            b = (y - self.y_mean)
            r1 += a * b
            c += a ** 2
            d += b ** 2

        r = r1 / math.sqrt(c * d)

        return r * self.calculate_standard_deviation(self.calc_list[:, 1]) / \
                self.calculate_standard_deviation(self.calc_list[:, 0])

    def calculate_intercept(self):
        # c = y| - m * x|

        return self.y_mean - self.slope * self.x_mean

    def get_regression(self):
        if self.intercept > 0: # Means intercept is positive.
            return f"f(x) = {self.slope} * x + {self.intercept}"
        elif self.intercept < 0: # Means intercept is negative.
            return f"f(x) = {self.slope} * x {self.intercept}"
        else: # Means intercept is 0 and we don't need to show it in the function.
            return f"f(x) = {self.slope} * x"

    def guess(self, x):
        return self.slope * x + self.intercept


def foo(x):
    # For development version

    return 3 * x - 5


def create_list(len):
    # For development version.

    new_list = np.zeros(shape=(len, 2), dtype=float)

    for i in range(0, len):
        x = random.random()
        y = foo(x)
        new_list[i] = [x, y]

    return new_list

try:
    dataset_len = int(input("How many sample data do you have?\n> "))
    # np_list = create_list(dataset_len)
    np_list = np.zeros(shape=(dataset_len, 2), dtype=float)
    for i in range(0, dataset_len):
        print(f"----- {i + 1} -----")
        np_list[i] = [int(input("Enter the X value: ")), int(input("Enter the Y value: "))]
        print()

    linear_model = LinearRegression(np_list)

    print(linear_model.get_regression())
    print(linear_model.guess(int(input("Enter the value you wanna try: "))))

except:
    print("Please enter valid inputs.")
