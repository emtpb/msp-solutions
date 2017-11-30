import numpy as np


def dft_msmp(signal):
    """calculate the dft of signal

    Args:
        signal (array_like): signal from that the dft should be calculated
    Returns:
        dft(array_like): dft of signal
    """
    n_max = np.size(signal)     # summation up to N=n_max
    dft = np.zeros(n_max, dtype=complex)
    n = np.arange(0, n_max)

    for k in range(0, n_max):
        exponential = np.exp(-1j*2*np.pi/n_max*k*n)
        dft[k] = sum(signal*exponential)        # calculate dft for each k

    return dft


def fft_msmp(signal):
    """calculate the fft of signal

    Args:
        signal (array_like): signal from that the fft should be calculated
    Returns:
        fft(array_like): fft of signal
    """
    n_max = np.size(signal)  # summation up to N=n_max
    if n_max == 1:          # base
        fft = signal
        return fft
    else:                   # recursive calculation
        signal_even = signal[0::2]
        transf_even = fft_msmp(signal_even)
        signal_odd = signal[1::2]
        transf_odd = fft_msmp(signal_odd)

        k = np.arange(0, n_max/2, dtype=int)
        fft = np.zeros(n_max, dtype=complex)

        # combine parts of fft
        fft[k] = transf_even + transf_odd*np.exp(-1j*2*np.pi*n_max*k)
        fft[int(n_max/2)+k] = transf_even - transf_odd*np.exp(-1j*2*np.pi*n_max*k)
        return fft
