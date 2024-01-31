import numpy as np
import matplotlib.pyplot as plt


def least_squares(x_values, inverse_values):
    plt.style.use('ggplot')
    degree = 2
    coeffs = np.polyfit(x_values, inverse_values, degree)
    poly = np.poly1d(coeffs)
    print('Coefficients of quadratic function: ', coeffs)
    print('Slope of the line of best fit:', coeffs[0])

    plt.figure(figsize=(20,10))
    plt.plot(x_values, inverse_values, 'b.')
    plt.plot(x_values, poly(x_values), 'r')

    plt.xlabel('X Values')
    plt.ylabel('Y Values')
    plt.title('Least Squares Approximation Graph')
    plt.savefig('least_squares.png')


if __name__ == '__main__':
    x_values = np.linspace(0, 1, 1000)
    sigma = 0.1
    inverse_values = 1 + x_values + sigma * np.random.random(len(x_values))
    least_squares(x_values, inverse_values)
