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

n_samples = 10000

# Select system to analyse by setting a function reference.
# Change to system1 .. system6 to select.
sys = sys.system1

# Create random binary sequence.
rbs = np.sign(np.random.randn(n_samples))

# Apply random binary sequence to selected system.
output = sys(rbs)

# Divide output spectrum by input spectrum.
norm_freq = np.linspace(0, 2, n_samples)
pp.figure()
pp.loglog(norm_freq, abs(np.fft.fft(output) / np.fft.fft(rbs)))
pp.xlabel('Normalized frequency $\Omega$')
pp.ylabel('$|G(\Omega)|$')
pp.grid(True)
pp.xlim(0, 0.5)

pp.show()
