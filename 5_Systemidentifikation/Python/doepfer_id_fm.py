import scipy.io
import numpy as np
import scipy.optimize as op
import matplotlib.pyplot as pp

mat = scipy.io.loadmat('../signals/doepfer_freq_mod.mat')
sig_out = np.squeeze(mat['output_signal'])
sig_out = sig_out - np.mean(sig_out)
sig_in = np.squeeze(mat['input_signal'])
time = np.squeeze(mat['time'])

start_f_mean = 0.0075
start_delta_f = 0.001
start_gain = 2
start_phase = 3 * np.pi / 2


def doepfer_model(input_signal, f_mean, delta_f, gain, phase):

    mod_signal = np.sin(2*np.pi * np.cumsum(f_mean + delta_f*input_signal) + phase)

    return mod_signal * gain


fig, ax = pp.subplots()
ax.plot(time, sig_in, label='input')
ax.plot(time, sig_out, label='output')
ax.plot(time, doepfer_model(sig_in, start_f_mean, start_delta_f, start_gain, start_phase), label='startparameter')
legend = ax.legend(loc='upper right')
pp.grid(True)


# costs in frequency domain
def costs_step_1(params):

    return np.sum((np.abs(np.fft.fft(sig_out, n=int(1e5))) -
                   np.abs(np.fft.fft(doepfer_model(sig_in, params[0], params[1], start_gain,
                                                   start_phase), n=int(1e5))))**2)


# identify frequencies in frequency domain:
opt_param_1 = op.fmin(costs_step_1, [start_f_mean, start_delta_f])
pp.figure()
pp.plot(time, doepfer_model(sig_in, opt_param_1[0], opt_param_1[1], start_gain, start_phase))
print(opt_param_1)


# costs in time domain
def costs_step_2(params):

    return np.sum((np.abs(sig_out) - np.abs(doepfer_model(sig_in, opt_param_1[0], opt_param_1[1],
                                                          params[0], start_phase)))**2)


opt_param_2 = op.fmin(costs_step_2, [start_gain])
pp.figure()
pp.plot(time, doepfer_model(sig_in, opt_param_1[0], opt_param_1[1], opt_param_2[0], start_phase))
print(opt_param_2)


def costs_step_3(params):

    return np.sum((sig_out - doepfer_model(sig_in, opt_param_1[0], opt_param_1[1],
                                           opt_param_2[0], params[0]))**2)


opt_param_3 = op.fmin(costs_step_3, [start_phase])
fig, ax = pp.subplots()
ax.plot(time, doepfer_model(sig_in, opt_param_1[0], opt_param_1[1], opt_param_2[0], opt_param_3[
    0]), label='Output using identified parameters')
print('f_mean & delta f:', opt_param_1)
print('Verstärkung gain:', opt_param_2)
print('Phase:', opt_param_3)

ax.plot(time, sig_out, label='output')
legend = ax.legend(loc='upper right')

pp.show()
