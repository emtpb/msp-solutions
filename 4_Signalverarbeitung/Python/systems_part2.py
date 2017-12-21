import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# Parameters from excercise question
f_s = 1e6
N = 2**11
f_base = 2e3

# Build corresponding time and frequency vectors
t = np.arange(0, N) / f_s
f = np.linspace(0, f_s, len(t))

# Create impulse input signal
u_in = np.zeros(t.shape)
u_in[0] = 1  # only the first element is 1

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

# Calculate impulse responses
b_system1 = np.array([0.1367, 0.1367])
a_system1 = np.array([1, -0.7265])
u_out_system1 = sys(b_system1, a_system1, u_in)

b_system2 = np.array([0.8633, -0.8633])
a_system2 = np.array([1, -0.7265])
u_out_system2 = sys(b_system2, a_system2, u_in)

# Plot the impulse responses
plt.figure()
plt.plot(t*1e6, u_in, 'o', label='Input $u_\mathrm{in}$')
plt.plot(t*1e6, u_out_system1, 'o', label='Output $u_\mathrm{out,1}$')
plt.plot(t*1e6, u_out_system2, 'o', label='Output $u_\mathrm{out,2}$')
plt.xlim((0, 15))
plt.ylim((-0.3, 1.1))
plt.xlabel('Time $t$ / µs')
plt.ylabel('Voltage $u$ / V')
plt.legend()
plt.grid()
plt.show()

# Calculate the transfer function
U_out_system1 = np.fft.fft(u_out_system1)
U_out_system2 = np.fft.fft(u_out_system2)

# Scale transfer function magnitude to dB
U_abs_system1 = 20*np.log10(abs(U_out_system1))
U_abs_system2 = 20*np.log10(abs(U_out_system2))

# Plot the transfer function (magnitude and phase)
plt.figure()
plt.subplot(2, 1, 1)
plt.semilogx(f[:N//2], U_abs_system1[:N//2], label='System 1')
plt.semilogx(f[:N//2], U_abs_system2[:N//2], label='System 2')
plt.semilogx(f[:N//2], np.ones((N//2,)) * -3, label='-3 dB threshold')
plt.xlim((5e2, 5e5))
plt.ylim((-20, 3))
plt.xlabel('Frequency $f$ / Hz')
plt.ylabel('|G(\mathrm{j}\omega)| / dB')
plt.grid(which='both')
plt.legend()

plt.subplot(2, 1, 2)
plt.semilogx(f[:N//2], np.angle(U_out_system1[:N//2], deg=True))
plt.semilogx(f[:N//2], np.angle(U_out_system2[:N//2], deg=True))
plt.xlim((5e2, 5e5))
plt.ylim((-100, 100))
plt.xlabel('Frequency $f$ / Hz')
plt.ylabel('$\\varphi(f)$ / °')
plt.grid(which='both')

plt.show()
