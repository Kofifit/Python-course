import numpy as np
from math import log, sqrt, pi, exp
from statistics import mean
import matplotlib.pyplot as plt

# Intialize true parameters to create distribution
# Mean value for gaussians
mu = np.array([-1, 4, 9])
# std value for gaussians
sigma = np.array([2, 3, 1])
# coefficients for gaussians
alpha = np.array([0.2, 0.3, 0.5])

# Intialize random parameters for model
mu_model = np.array([-1, 4, 9])
sigma_model = np.array([2, 3, 1])
alpha_model = np.array([0.2, 0.3, 0.5])

# Intialixe important parameters for algorithm
# Number of samples
sample_num = 200
# Define fx vector
fx = []
# Number of iterations
iter_num = np.arange(50)
# Define liklihood vector (length as number of iterations)
likelihood = np.zeros(max(iter_num) + 1)

# Create distribution with real parameters

# Run for each gaussian
for i in range(0, len(mu)):
    # Find number of observations from current gaussian
    num = int(sample_num * alpha[i])
    # Create observations for current gaussian
    x = np.random.normal(mu[i], sigma[i], num)
    # Add observations to fx vector
    fx = np.concatenate([fx, x])


for iteration in iter_num:

    # E-step
    # Define probability density matrix of zeros
    pdf = np.zeros([sample_num, len(mu)])
    # Run on all observations in fx vector
    for i in range(0, len(fx)):
        # likelihood for observation in each gaussian
        for j in range(0, len(mu)):
            # Calculate pdf for current gaussian
            d = (fx[i] - mu_model[j]) / abs(sigma_model[j])
            pdf[i][j] = (1 / sqrt(2 * pi) * abs(sigma_model[j])) * exp(-d * d / 2)
            pdf[i][j] = alpha_model[j] * pdf[i][j]
        # Calcualte observation density for all gaussians
        density = sum(pdf[i, :])
        # Normalize pdf for each gaussian
        pdf[i][:] /= density
        # Add current observation density to log likelihood
        likelihood[iteration] += log(density)

    # M-step:
    # update patameters of each guassian
    for i in range(0, len(mu)):
        # std update
        sigma_model[i] = sqrt(np.sum(pdf[:, i] * ((fx - mu_model[i]) ** 2)) / np.sum(pdf[:, i]))
        # mean update
        mu_model[i] = np.sum(pdf[:, i] * fx) / np.sum(pdf[:, i])
        # alpha update
        alpha_model[i] = np.sum(pdf[:, i]) / len(fx)

# print final parameters for all gaussians
print(mu_model, sigma_model, alpha_model)

# Plot log likelihood as a function of the iterations
plt.plot(iter_num, likelihood)
plt.xlabel("Number of iterations")
plt.ylabel("likelihood")
plt.title("200 Samples")
plt.show()
