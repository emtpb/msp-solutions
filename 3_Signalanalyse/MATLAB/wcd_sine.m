% calculate wvd of sine signals

clear all
close all
clc

% parameters
sampl_freq = 100;       % sampling frequency
N = 1024;               %  number of samples
t = (0:N-1)/sampl_freq; % time vector

% create signal
f_1 = 1;
f_2 = 5;

y_1 = sin(2*pi*f_1.*t);
y_2 = sin(2*pi*f_2.*t);
y = y_1;

% plot signal
figure
plot(t, y)
xlabel('Time {\itt} / s')

% Wigner-Ville-Distribution
[wv, f, t] = wvd(y, 1, N/2, sampl_freq);

figure
pcolor(t, f, abs(wv)), shading flat
xlabel('Time {\itt} / s')
ylabel('Frequency {\itf} / Hz')
ylim([0, 6])
