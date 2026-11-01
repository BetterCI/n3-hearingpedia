import numpy as np
from scipy.special import expit
from scipy.optimize import minimize
rng = np.random.default_rng(20261102)
x = rng.normal(size=(600, 2))
A = np.column_stack([np.ones(600), x])
y = rng.binomial(1, expit(-.3 + 1.1*x[:, 0] - .8*x[:, 1]))
T, H, lam = np.arange(400), np.arange(400, 600), .05

def loss(beta):
    z = A[T] @ beta
    return np.mean(np.logaddexp(0, z) - y[T]*z) + lam/2*(beta[1:] @ beta[1:])

def grad(beta):
    return A[T].T @ (expit(A[T] @ beta)-y[T])/len(T) + lam*np.r_[0., beta[1:]]

fit = minimize(loss, np.zeros(3), jac=grad, method="BFGS",
               options={"gtol": 1e-9})
assert fit.success or np.linalg.norm(grad(fit.x)) < 1e-7
z = A[H] @ fit.x
print(fit.x)
print("test log loss", np.mean(np.logaddexp(0, z)-y[H]*z))
print("test accuracy", np.mean((z >= 0) == y[H]))
