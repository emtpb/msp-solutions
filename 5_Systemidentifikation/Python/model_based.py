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
import matplotlib.pyplot as pp
import scipy.signal as sig
from mpl_toolkits.mplot3d import Axes3D

system = sys.system4

# Create chirp test signal
test_sig = sig.chirp(np.linspace(0, 1000, 1000), 0.0001, 1000, 0.05, method='quadratic')
# Calculate system response.
test_response = system(test_sig)


# Plot test signal and response.
pp.plot(test_sig)
pp.plot(test_response)
pp.legend(['Input signal $x_\mathrm{in}$', 'Output signal $x_\mathrm{out}$'])
pp.xlabel('Index $n$')


def forward_model(sig_in, cutoff_frequ, order):
    """Forward model function (a low-pass filter).

    Args:
        sig_in: Input signal
        cutoff_frequ: Normalized cutoff frequency.
        order: Order of the filter.

    Returns:
        Output signal of the model.
    """

    b, a = sig.butter(order, cutoff_frequ)
    return sig.lfilter(b, a, sig_in)


def cost_fctn(sig_out, sig_in, cutoff_frequ, order):
    """Cost function to minimize.

    Args:
        sig_out: Output signal of the model.
        sig_in: Input signal of the model.
        cutoff_frequ: Normalized cutoff frequency.
        order: Order of the filter.

    Returns:
        Costs as a scalar float value.
    """

    return np.sum((sig_out - forward_model(sig_in, cutoff_frequ, order))**2)


# Create vectors for parameters.
cutoff_frequ_vector = np.linspace(0.001, 0.04, 200)
order_vector = np.linspace(1, 6, 6)

# Initialize matrix for cost function values.
cost_fctn_evaled = np.zeros((len(cutoff_frequ_vector), len(order_vector)))

# Evaluate cost function.
for ii in range(len(cutoff_frequ_vector)):
    for jj in range(len(order_vector)):
        cost_fctn_evaled[ii, jj] = cost_fctn(test_response, test_sig, cutoff_frequ_vector[ii],
                                             order_vector[jj])

# Create meshgrid for surface plot.
xs, ys = np.meshgrid(order_vector, cutoff_frequ_vector)

# Plot values of cost function.
fig = pp.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(xs, ys, cost_fctn_evaled, vmin=0, vmax=np.max(cost_fctn_evaled),
                       cmap='viridis')
pp.xlabel('Filter order $n_\mathrm{f}$')
pp.ylabel('Normalized cut-off frequency $\Omega_\mathrm{c}$')
ax.set_zlabel('Value of cost function')

pp.show()
