import numpy as np
import matplotlib.pyplot as plt
import time
import fourier_msmp as fourier

# define parameters
f_0 = 1
n_max = 2048
number_periodes = 1
sampl_freq = n_max/number_periodes

n = np.arange(0, n_max)

# generate and plot y
y = np.cos(2*np.pi*f_0*n/sampl_freq)

plt.figure()
plt.stem(n, y)
plt.xlabel('index $n$')
plt.ylabel('y')

# calculate dfts using different algorithms
# dft_msmp
t = time.time()
dft = fourier.dft_msmp(y)
dft_t = time.time()-t
# fft_msmp
t = time.time()
ft = fourier.fft_msmp(y)
ft_t = time.time()-t
# build in python fft
t = time.time()
ft_python = np.fft.fft(y)
ft_python_t = time.time()-t

# plot results from different algorithms
plt.figure()
plt.stem(abs(dft), 'r', label='DFT')
plt.stem(abs(ft), 'g', label='FFT')
plt.stem(abs(ft_python), 'g', label='build-in FFT')
plt.xlim(-0.5, n_max+0.5)
plt.xlabel('index $k$')
plt.legend()

# calculate dft for different length of y
power_max = 12      # calculate 2**power_max-fft
powers = np.arange(1, power_max+1, dtype=int)
# init
dft_time = np.zeros(power_max)
ft_time = np.zeros(power_max)
ft_python_time = np.zeros(power_max)
# theoretical run time
ideal_dft = np.zeros(power_max)
ideal_fft = np.zeros(power_max)

for power in powers:
    n = np.arange(0, 2**power)

    y = np.cos(2*np.pi*f_0*n/sampl_freq)
    t = time.clock()
    # dft
    dft = fourier.dft_msmp(y)
    dft_time[power-1] = time.clock() - t
    # fft
    t = time.time()
    ft = fourier.fft_msmp(y)
    ft_time[power-1] = time.time() - t
    # build in fft
    t = time.time()
    ft_python = np.fft.fft(y)
    ft_python_time[power-1] = time.time() - t

    ideal_dft[power-1] = (2**power)**2
    ideal_fft[power-1] = (2**power)*power

# plot computing time
plt.figure()
plt.plot(2**(np.arange(1, power_max+1)), dft_time, 'b', label='DFT')
plt.plot(2**(np.arange(1, power_max+1)), ft_time, 'r', label='FFT')
plt.xlabel('length of transformed signal $n_{max}$')
plt.ylabel('computing time $t_{comp}$ / s')
plt.legend()

plt.figure()
plt.plot(2**(np.arange(1, power_max+1)), ideal_dft, 'b', label='DFT ideal')
plt.plot(2**(np.arange(1, power_max+1)), ideal_fft, 'r', label='DFT ideal')
plt.xlabel('length of transformed signal $n_{max}$')
plt.ylabel('computing time $t_{comp}$ / s')
plt.legend()

plt.figure()
plt.plot(2**(np.arange(1, power_max+1)), ft_python_time)
plt.xlabel('length of transformed signal $n_{max}$')
plt.ylabel('computing time $t_{comp}$ / s')
plt.title('buide in FFT')

plt.show()
