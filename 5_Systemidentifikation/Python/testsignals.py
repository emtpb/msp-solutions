import numpy as np
import matplotlib.pyplot as pp

n_samples = 5000

# create signals
# gaussian (normal) distribution
gaussian = np.random.randn(n_samples)
# uniform distribution
uniform = 2*np.random.rand(n_samples) - 1
# random binary sequence
rbs = np.sign(gaussian)

pp.figure()
pp.subplot(311)
pp.plot(gaussian)
pp.title('gaussian')
pp.subplot(312)
pp.plot(uniform)
pp.title('uniform')
pp.ylim(-2, 2)
pp.subplot(313)
pp.plot(rbs)
pp.title('RBS')
pp.ylim(-2, 2)
pp.xlabel('Index $n$')
pp.grid(True)


# plot spectra
norm_freq = np.linspace(0, 2, n_samples)
pp.figure()
pp.plot(norm_freq, abs(np.fft.fft(gaussian)))
pp.plot(norm_freq, abs(np.fft.fft(uniform)))
pp.plot(norm_freq, abs(np.fft.fft(rbs)))
pp.xlim(0, 1)
pp.xlabel('Normalized frequency $\Omega$')
pp.legend(('gaussian', 'uniform', 'RBS'))
pp.grid(True)


# plot auto correlation
lag_samples = np.concatenate((np.linspace(-(n_samples - 1), 0, n_samples - 1, endpoint=False),
                              np.linspace(0, n_samples, n_samples, endpoint=False)))
pp.figure()
pp.plot(lag_samples, np.correlate(gaussian, gaussian, 'full') /
        max(np.correlate(gaussian, gaussian, 'full')))
pp.plot(lag_samples, np.correlate(uniform, uniform, 'full') /
        max(np.correlate(uniform, uniform, 'full')))
pp.plot(lag_samples, np.correlate(rbs, rbs, 'full') /
        max(np.correlate(rbs, rbs, 'full')))
pp.legend(('gaussian', 'uniform', 'RBS'))
pp.xlabel('Index lag $\Delta n$')
pp.ylabel('Normalized autocorrelation')
pp.grid(True)

pp.show()
