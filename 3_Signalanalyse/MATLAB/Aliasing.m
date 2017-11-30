clear all
close all
clc

%% load and plot
% read file
[y, sampl_freq] = audioread('r2d2whereareyou.wav');

n = length(y);                   % signal length
delta_t = 1/sampl_freq;
t = 0:delta_t:(n-1)/sampl_freq;  % time vector

% plot signal
figure
plot(t, y)
xlabel('Time {\itt} / s')
ylabel('Original singal')

% play signal
sound(y, sampl_freq)

% spectrum
delta_f = sampl_freq/n;
f = 0:delta_f:sampl_freq-delta_f;
ft = abs(fft(y));

figure
plot(f, ft)
xlabel('frequency {\itf} / Hz')
ylabel('spectrum of original signal')


%% downsample
p = 2;      % downsampling factor
sampl_freq_downsample = sampl_freq/p;   % new downsampling frequency
y_downsample = downsample(y, p);
n_downsample = length(y_downsample);
t = 0:1/sampl_freq_downsample:(n_downsample-1)/sampl_freq_downsample;

figure
plot(t, y_downsample, 'r')
xlabel('Time {\itt} / s')
ylabel(['signal sampled with ', num2str(sampl_freq_downsample), ' Hz)'])

delta_f_downsample = sampl_freq_downsample/n_downsample;
f_downsample = 0:delta_f_downsample:sampl_freq_downsample-delta_f_downsample;
figure
plot(f_downsample, abs(fft(y_downsample)), 'r')
xlabel('Frequency {\itf} / Hz')
ylabel(['spectrum of signal samples with ', num2str(sampl_freq_downsample), ' Hz)'])

sound(y_downsample, sampl_freq_downsample)
% audiowrite('downsample.wav', y_downsample, sampl_freq_downsample);
