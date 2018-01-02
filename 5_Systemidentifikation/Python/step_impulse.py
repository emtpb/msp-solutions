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

# Select system to analyse by setting a function reference.
# Change to system1 .. system6 to select.
system = sys.system6

# Create impulse signal.
imp = np.zeros(1000)
imp[10] = 1

# Create step signal.
step = np.zeros(1000)
step[10:] = 1

pp.figure()
# Plot normalized impulse response.
pp.plot(system(imp) / np.max(system(imp)))
# Plot normalized step response.
pp.plot(system(step) / np.max(system(step)))
pp.legend(('Impulse response', 'Step response'))
pp.xlabel('Index $n$')
pp.grid(True)

pp.figure()
# Plot absolute value of transfer function by transforming impulse response.
pp.loglog(abs(np.fft.fft(system(imp))))
pp.xlabel('Normalized frequency $\Omega$')
pp.ylabel('$|G(\Omega)|$')
pp.grid(True)
# Cut to relevant part (~lower quarter).
pp.xlim(0, 250)

pp.show()
