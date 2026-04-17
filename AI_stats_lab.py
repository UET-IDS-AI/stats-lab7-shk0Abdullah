"""
AI_stats_lab.py

Lab: Uniform Random Variable Analysis
"""

import numpy as np


def uniform_analysis(a, n_samples=10000):
    """
    Returns:
    (
        theoretical_mean,
        theoretical_variance,
        sample_mean,
        sample_variance,
        mean_error,
        variance_error,
        transformed_mean,
        transformed_variance
    )
    """
    # Theoretical values for uniform distribution on [0, a]
    theoretical_mean = a / 2
    theoretical_variance = (a ** 2) / 12
    
    # Generate random samples
    samples = np.random.uniform(0, a, n_samples)
    
    # Sample statistics
    sample_mean = np.mean(samples)
    sample_variance = np.var(samples)
    
    # Errors (absolute differences)
    mean_error = abs(sample_mean - theoretical_mean)
    variance_error = abs(sample_variance - theoretical_variance)
    
    # Transformation Y = 2X + 1 (theoretical values)
    transformed_mean = 2 * theoretical_mean + 1
    transformed_variance = 4 * theoretical_variance
    
    return (
        theoretical_mean,
        theoretical_variance,
        sample_mean,
        sample_variance,
        mean_error,
        variance_error,
        transformed_mean,
        transformed_variance
    )


if __name__ == "__main__":
    print("Implement uniform_analysis(a, n_samples=10000)")
