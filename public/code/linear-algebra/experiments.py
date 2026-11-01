"""Acoustic examples for learning linear algebra. Synthetic data, no recordings.

Run: python experiments.py
Requires NumPy. run_experiments() also returns arrays for reproducible figures.
"""
import json
import numpy as np


def delay_matrix(x, length):
    """Valid rows only: output times length-1 through len(x)-1."""
    index = np.arange(length - 1, len(x))
    return np.column_stack([x[index - k] for k in range(length)])


def ridge(A, y, lam):
    """Augmented least squares, with no explicit inverse or normal matrix."""
    return np.linalg.lstsq(
        np.vstack([A, np.sqrt(lam) * np.eye(A.shape[1])]),
        np.r_[y, np.zeros(A.shape[1])], rcond=None)[0]


def run_experiments():
    fs = 8000
    nonorthogonal = []
    for count in (8, 80):
        n = np.arange(count)
        B = np.column_stack([np.cos(2*np.pi*1000*n/fs), np.cos(2*np.pi*1100*n/fs)])
        y = B @ np.array([.6, .3])
        separate = (B.T @ y) / np.sum(B*B, axis=0)
        joint = np.linalg.lstsq(B, y, rcond=None)[0]
        np.testing.assert_allclose(joint, [.6, .3], atol=1e-12)
        nonorthogonal.append({'samples': count, 'gram': (B.T@B).tolist(),
                              'separate': separate.tolist(), 'joint': joint.tolist(),
                              'condition_number': float(np.linalg.cond(B, 2))})
    np.testing.assert_allclose(nonorthogonal[1]['separate'], [.6, .3], atol=1e-12)

    n = np.arange(8)
    a = np.cos(2*np.pi*1000*n/fs)
    b = np.cos(2*np.pi*2000*n/fs)
    sine = np.sin(2*np.pi*1000*n/fs)
    phase_mix = .6*sine + .3*b
    phase_coefficients = [float(a@phase_mix/(a@a)), float(sine@phase_mix/(sine@sine))]
    np.testing.assert_allclose(phase_coefficients, [0, .6], atol=1e-12)

    truth = np.array([1., .2])
    modal = []
    for rho in (.5, .95, .995):
        G = np.array([[1., rho], [rho, 1.]])
        observed = G@truth + np.array([.001, -.001])
        plain = np.linalg.solve(G, observed)
        np.testing.assert_allclose(plain-truth, [.001/(1-rho), -.001/(1-rho)], atol=1e-12)
        common = np.linalg.solve(G, G@truth + np.array([.001, .001]))
        np.testing.assert_allclose(common-truth, np.ones(2)*.001/(1+rho), atol=1e-12)
        U, singular, Vh = np.linalg.svd(G, full_matrices=False)
        np.testing.assert_allclose((U*singular)@Vh, G, atol=1e-12)
        modal.append({'rho': rho, 'condition_number': float(np.linalg.cond(G, 2)),
                      'singular_values': singular.tolist(), 'direct': plain.tolist(),
                      'common_noise_solution': common.tolist(),
                      'ridge_1e-5': ridge(G, observed, 1e-5).tolist(),
                      'ridge_1e-3': ridge(G, observed, 1e-3).tolist()})

    rng = np.random.default_rng(20261101)
    length, count, noise_sd = 65, 2048, .02
    h = np.zeros(length)
    h[[0, 24, 56]] = [.8, .3, -.15]
    x_train = rng.normal(0, .25, count)
    A = delay_matrix(x_train, length)
    train_clean = A@h
    train_observed = train_clean + rng.normal(0, noise_sd, len(A))
    estimated, _, rank, _ = np.linalg.lstsq(A, train_observed, rcond=None)
    Q, R = np.linalg.qr(A, mode='reduced')
    np.testing.assert_allclose(np.linalg.solve(R, Q.T@train_observed), estimated, atol=1e-12)
    np.testing.assert_allclose(A.T@(train_observed-A@estimated), 0, atol=1e-10)
    x_validation = rng.normal(0, .25, count)
    Av = delay_matrix(x_validation, length)
    validation_clean = Av@h
    validation_observed = validation_clean + rng.normal(0, noise_sd, len(Av))
    validation_prediction = Av@estimated
    constant = delay_matrix(np.ones(count), length)
    single_tone = delay_matrix(np.cos(2*np.pi*1000*np.arange(count)/fs), length)
    tone_rank = np.linalg.matrix_rank(single_tone, tol=1e-9)
    assert rank == length and np.linalg.matrix_rank(constant) == 1 and tone_rank == 2
    rmse = lambda e: float(np.sqrt(np.mean(e*e)))
    echo = {'sample_rate_hz': fs, 'input_samples': count, 'filter_length': length,
            'design_shape': list(A.shape), 'seed': 20261101, 'input_sd': .25, 'noise_sd': noise_sd,
            'true_nonzero_indices': [0, 24, 56], 'true_nonzero_gains': [.8, .3, -.15],
            'estimated_gains_at_paths': estimated[[0, 24, 56]].tolist(),
            'coefficient_rmse': rmse(estimated-h), 'train_observed_rmse': rmse(train_observed-A@estimated),
            'validation_observed_rmse': rmse(validation_observed-validation_prediction),
            'validation_clean_rmse': rmse(validation_clean-validation_prediction),
            'random_input_rank': int(rank), 'constant_input_rank': 1, 'tone_input_rank': int(tone_rank),
            'tone_rank_absolute_tolerance': 1e-9, 'lstsq_rcond': None,
            'random_design_condition': float(np.linalg.cond(A, 2))}

    X = np.column_stack([.6*a+.2*b, .6*a-.2*b])
    Xc = X-X.mean(axis=0)
    covariance = Xc.T@Xc/len(Xc)
    eigenvalues, basis = np.linalg.eigh(covariance)
    order = np.argsort(eigenvalues)[::-1]
    eigenvalues, basis = eigenvalues[order], basis[:, order]
    scores = Xc@basis
    np.testing.assert_allclose(scores@basis.T, Xc, atol=1e-12)
    np.testing.assert_allclose(eigenvalues, [.36, .04], atol=1e-12)
    report = {'data_type': 'synthetic acoustic teaching experiments', 'numpy_version': np.__version__,
              'nonorthogonal': nonorthogonal, 'phase_coefficients': phase_coefficients,
              'modal_noise': modal, 'echo': echo,
              'pca_eigenvalues_1_over_N': eigenvalues.tolist(), 'pca_first_variance_fraction': .9}
    arrays = {'h_true': h, 'h_estimated': estimated, 'validation_clean': validation_clean,
              'validation_observed': validation_observed, 'validation_prediction': validation_prediction}
    return report, arrays


if __name__ == '__main__':
    result, _ = run_experiments()
    print(json.dumps(result, ensure_ascii=False, indent=2))
