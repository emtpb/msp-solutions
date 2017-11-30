clear all
close all
clc

% load data
[t, y] = textread('H1.txt', '%f %f', 'commentstyle', 'shell');

figure
plot(t, y)
xlabel('time {\itt} / s')
ylabel('strain \epsilon \cdot 1e21')

sampl_freq = 1/(t(2)-t(1));

% scaling parameter a
scales = linspace(1/10, 10, 1000);  

% define wavelet and its paramters
fb = 1/50/2;
fc = 50;
waveletFun = @(f) exp(-fb^2 * pi^2 *... 
        (f - fc).^2);

% caluclate Wavelet Transform
wt = waveletTransform(y, sampl_freq, scales, waveletFun);

f = fc./scales;
figure
pcolor(t, f, abs(wt)), shading flat
xlabel('Time {\itt} / s')
ylabel('Frequency {\itf} / Hz')

%%
sig.val = y;
sig.period = 1/sampl_freq;
cwtstruct = cwtft(sig);