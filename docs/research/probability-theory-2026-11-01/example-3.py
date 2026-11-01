from math import sqrt
from statistics import NormalDist
from scipy.stats import beta

k, n = 30, 40
p = k/n
z = NormalDist().inv_cdf(0.975)
den = 1 + z*z/n
center = (p + z*z/(2*n))/den
half = z*sqrt(p*(1-p)/n + z*z/(4*n*n))/den
wilson = (center-half, center+half)
posterior = beta(1+k, 1+n-k)
credible = posterior.ppf([0.025, 0.975])
print("样本正确率与Wilson区间:", p, wilson)
print("均匀先验下的后验均值与可信区间:", posterior.mean(), credible)
assert abs(wilson[0] - 0.5980603857923197) < 1e-12
assert abs(posterior.mean() - 31/42) < 1e-12
