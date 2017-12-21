import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# Parameters from excercise question
f_s = 1e6
N = 2**11
f_base = 2e3

# Build corresponding time vector
t = np.arange(0, N) / f_s

# Create rectangular test signal
u_test = np.sign(np.sin(2*np.pi*f_base*t))

# Build sys() function
def sys(b, a, u_in):
    # Initialize output data (same length as input)
    u_out = np.zeros(u_in.shape)

    # For all elements...
    for n in range(0, u_in.shape[0]):
        # create a temporary accumulation variable
        tmp = 0

        # For all elements in b...
        for p, b_p in enumerate(b):
            if p <= n:  # ensure >= 0 indices in u_in
                # add the current feed-forward term
                tmp = tmp + b_p * u_in[n-p]

        # For all elements in a...
        for q, a_q in enumerate(a[1:], start=1):
            if q <= n:  # ensure >= 0 indices in u_in
                # subtract the current feed-back term
                tmp = tmp - a_q * u_out[n-q]

        u_out[n] = tmp

    u_out = u_out / a[0]
    return u_out

# Apply own sys() function to test signal
b_system1 = np.array([0.1367, 0.1367])
a_system1 = np.array([1, -0.7265])
u_out_system1 = sys(b_system1, a_system1, u_test)

# Ensure sys is working correctly (compare to scipy's implementation)
u_out_check = signal.lfilter(b_system1, a_system1, u_test)
if not np.allclose(u_out_system1, u_out_check):
    print('Oops. sys() does not do what it''s supposed to do.')

# Visualize the signal
plt.figure()
plt.plot(t*1e3, u_test)
plt.plot(t*1e3, u_out_system1)
plt.xlim(0, 2)
plt.ylim(-1.1, 1.1)
plt.xlabel('Time $t$ / ms')
plt.ylabel('Voltage $u$ / V')
plt.show()

# Do the same thing for the second set of parameters
b_system2 = np.array([0.8633, -0.8633])
a_system2 = np.array([1, -0.7265])
u_out_system2 = sys(b_system2, a_system2, u_test)

plt.figure()
plt.plot(t*1e3, u_test)
plt.plot(t*1e3, u_out_system2)
plt.xlim(0, 2)
plt.ylim(-1.1, 1.1)
plt.xlabel('Time $t$ / ms')
plt.ylabel('Voltage $u$ / V')
plt.show()
