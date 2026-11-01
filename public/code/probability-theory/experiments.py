"""Probability through sound: synthetic examples, not participant measurements.

Requires Python 3.10+, NumPy and SciPy. Run: python experiments.py
All parameters and seeds match the article. No files are read or written.
"""
from math import comb, erf, sqrt, log
from statistics import NormalDist
import numpy as np
from scipy import stats


def main():
    Phi = lambda z: (1 + erf(z / sqrt(2))) / 2
    tail = sum(comb(40, k) for k in range(30, 41)) / 2**40
    print('One-sided chance tail, at least 30/40:', tail)
    print('Normal pressure within +/-0.01 Pa, sigma=0.02 Pa:', Phi(.5)-Phi(-.5))
    for prior in (.2, .02):
        posterior = .8*prior/(.8*prior + .1*(1-prior))
        print('P(signal | report yes), prior=', prior, ':', posterior)

    # At one fixed time, rows are independently simulated complete experiments.
    rng = np.random.default_rng(20261105)
    sets, M, sigma, rho = 50000, 16, .2, .5
    ind = rng.normal(0, sigma, (sets, M))
    common = rng.normal(0, sigma*sqrt(rho), (sets, 1))
    private = rng.normal(0, sigma*sqrt(1-rho), (sets, M))
    sd_ind = ind.mean(axis=1).std(ddof=1)
    sd_shared = (common+private).mean(axis=1).std(ddof=1)
    theoretical = sigma*sqrt(rho+(1-rho)/M)
    assert abs(sd_ind-sigma/sqrt(M)) < .002
    assert abs(sd_shared-theoretical) < .003
    print('Average SD, independent:', sd_ind, 'theory:', sigma/sqrt(M))
    print('Average SD, shared noise:', sd_shared, 'theory:', theoretical)

    # One latent listener type is selected for the entire set of responses.
    # Conditional independence does not imply marginal independence.
    latent_p = rng.choice([.6, .9], size=200000)
    x = rng.binomial(1, latent_p)
    y = rng.binomial(1, latent_p)
    cov = np.cov(x, y, ddof=0)[0, 1]
    assert abs(cov-.0225) < .002
    print('Cross-trial covariance from shared listener type:', cov, 'theory:', .0225)

    F, H = stats.norm.sf(1), stats.norm.sf(-.5)
    dprime = stats.norm.ppf(H)-stats.norm.ppf(F)
    pc = stats.norm.cdf(dprime/sqrt(2))
    assert abs(dprime-1.5) < 1e-12
    print('Equal-variance Gaussian F, H, d-prime, 2IFC correct:', F, H, dprime, pc)
    gamma, upper_gap, alpha, scale, q = .5, .02, 0., 3., .75
    u = (q-gamma)/(1-gamma-upper_gap)
    threshold = alpha+scale*log(u/(1-u))
    print('Logistic 75% threshold (dB):', threshold)

    k, n = 30, 40
    p = k/n
    z = NormalDist().inv_cdf(.975)
    den = 1+z*z/n
    center = (p+z*z/(2*n))/den
    half = z*sqrt(p*(1-p)/n+z*z/(4*n*n))/den
    posterior = stats.beta(1+k, 1+n-k)
    print('Sample fraction, Wilson 95% CI:', p, (center-half, center+half))
    print('Beta(1,1) prior: posterior mean and 95% equal-tailed credible interval:',
          posterior.mean(), posterior.ppf([.025,.975]))
    print('CI and credible interval have different interpretations; see article.')


if __name__ == '__main__':
    main()
