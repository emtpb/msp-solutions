import numpy as np
import scipy.io as sio
from scipy import signal
from matplotlib import pyplot as plt

from findpeaks import findpeaks
from phase_compensation import phase_compensation

# Load measurement data
data_file = sio.loadmat('preprocessing_data.mat')
t = data_file['t']
u = data_file['u']

# Preserve original signal for later comparison
# Note: Make a copy instead of only a reference to the same vector!
u_orig = u.copy()

# Detrend & find envelope
u = signal.detrend(u, axis=0)
u_env = np.abs(signal.hilbert(u, axis=0))

# Visually compare original, detrended signal and envelope
plt.figure()
plt.plot(t*1e3, u_orig, label='Original')
plt.plot(t*1e3, u, label='Detrended')
plt.plot(t*1e3, u_env, label='Envelope')
plt.legend()
plt.xlabel('Time $t$ / ms')
plt.ylabel('Voltage $u$ / V')
plt.show()

# Remove irrelevant data parts
# Note: The limits can be determined by finding the section of the envelope that
#       less noisy.
mask = np.logical_and(t >= 1.05e-4, t <= 1.4e-4)
t = t[mask]
u = u[mask]

# Determine amplitude...
# ...either via envelope (larger error)
u_hat_1 = np.mean(np.abs(signal.hilbert(u)))

# ...or via findpeaks
idx_max, u_max = findpeaks(u)
u_hat_2 = np.mean(u_max)

# Visualize the relevant signal part and the detected amplitudes
plt.figure()
plt.plot(t*1e3, u, label='Extracted signal')
plt.plot(t*1e3, np.ones(u.shape) * u_hat_1, label='Amplitude (via envelope)')
plt.plot(t*1e3, np.ones(u.shape) * u_hat_2, label='Amplitude (via findpeaks)')
plt.legend()
plt.xlabel('Time $t$ / ms')
plt.ylabel('Voltage $u$ / V')
plt.show()

# Determine signal frequency
# Note: This solution is in time domain, but frequency domain also works well.
delta_t = np.mean(np.diff(t[idx_max]))
f_sig = 1/delta_t

# Determine phase offset
phi = phase_compensation(t, u, f_sig)

# Compare simulated and measured signal
u_sim = u_hat_2 * np.sin(2*np.pi*f_sig*t - phi)

plt.figure()
plt.plot(t*1e3, u, label='Measurement')
plt.plot(t*1e3, u_sim, label='Simulation')
plt.legend()
plt.xlabel('Time $t$ / ms')
plt.ylabel('Voltage $u$ / V')
plt.show()
