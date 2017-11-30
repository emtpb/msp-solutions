clear all
close all
clc

% read signal
[y, sampl_freq] = audioread('hello.wav');

% plot signal
t = (0:length(y)-1)/sampl_freq;
figure
plot(t, y)
xlabel('Zeit {\itt} / s')

% calculate spectrogram
[spec, f, t] = spectrogram(y, 512, 511, [], sampl_freq);

% plot logarithmic spectrogram
figure,
pcolor(t, f, log(abs(spec).^2)), shading flat
xlabel('Zeit {\itt} / s')
ylabel('Frequenz {\itf} / Hz')
set(gca, 'yscale', 'log') 
