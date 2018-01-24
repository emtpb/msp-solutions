"""
IMPORTANT:
Import the .pyc module matching your Python version (e.g. systems_34 for python 3.4). If
modules for versions other than the supplied are required, contact Leander or install a newer
version.
If you get a "ImportError: bad magic number...", your Python version and the .pyc module's
version are mismatched.
"""
import systems_34 as sys
import numpy as np
import scipy.optimize as opt
import scipy.signal as sig

system = sys.system4

# Create chirp test signal.
test_sig = sig.chirp(np.linspace(0, 1000, 1000), 0.0001, 1000, 0.05, method='quadratic')
# Calculate system response.
test_response = system(test_sig)


def forward_model(sig_in, cutoff_frequ, order):
    """Forward model function (a low-pass filter).

    Args:
        sig_in: Input signal
        cutoff_frequ: Normalized cutoff frequency.
        order: Order of the filter.

    Returns:
        Output signal of the model.
    """

    # Limit cut-off frequency values 0< .. <1
    cutoff_frequ = np.clip(cutoff_frequ, np.finfo(float).eps, 1 - np.finfo(float).eps)

    b, a = sig.butter(order, cutoff_frequ)

    return sig.lfilter(b, a, sig_in)


def cost_fctn(cutoff_frequ):
    """Cost function to minimize.

    Args:
        cutoff_frequ: Normalized cutoff frequency.

    Returns:
        Costs as a scalar float value.
    """

    return np.sum((test_response - forward_model(test_sig, cutoff_frequ, 1))**2)


# Start optimization with initial value of cut-off frequency 0.5.
cutoff_frequ_opt = opt.fmin(cost_fctn, 0.5)

# Print result.
print(cutoff_frequ_opt)
