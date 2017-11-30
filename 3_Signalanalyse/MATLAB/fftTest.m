clear all
close all
clc

%% calculated DFT using different algorithms
% define parameters
f_0 = 1;
N = 2048;
number_periodes = 1;
sampl_freq = N/number_periodes;

n = 0:N-1;

% generate and plot y
y = cos(2*pi*f_0.*n/sampl_freq);

figure
stem(n, y, 'LineWidth', 2)
xlabel('Index {\itn}')

% calculate dfts using different algorithms
% dft_msmp
tic
dft = dftMSMP(y);
dft_time = toc;
% fft_msmp
tic
ft = fftMSMP(y);
ft_time = toc;
% build-in fft
% tic
% ft_ML = fft(y);
% ft_ML_time = toc;

% plot results from different algorithms
figure
hold all
stem(abs(dft), 'LineWidth', 2)
stem(abs(ft), 'LineWidth', 2)
% stem(abs(ft_ML), 'LineWidth', 2)
legend('DFT MSMP', 'FFT MSMP')
xlabel('Index {\itk}')

disp(['Time for DFT: ', num2str(dft_time), 's'])
disp(['Time for FFT: ', num2str(ft_time), 's'])
%% calculate dft for different length of y

for N = 1:15
    n = 0:2^N-1;

    y = cos(2*pi*f_0.*n/sampl_freq);
    
    % dft
    tic
    [dft] = dftMSMP(y);
    dft_time(N) = toc;
    % fft
    tic
    ft = fftMSMP(y);
    ft_time(N) = toc;
    % build in dft
    tic
    ft_ML = fft(y);
    ft_ML_time(N) = toc;
    
    idealDFT(N) = (2^N)^2;
    idealFFT(N) = (2^N)*N;
end

% plot computing time
figure
hold all
plot(2.^(1:N), dft_time, 'b', 'LineWidth', 2)
plot(2.^(1:N), ft_time, 'r', 'LineWidth', 2)
xlabel('Laufzeit {\itt}_{comp}')
legend('DFT', 'FFT')
figure
hold all
plot(2.^(1:N), idealDFT, 'b--', 'LineWidth', 2)
plot(2.^(1:N), idealFFT, 'r--', 'LineWidth', 2)
xlabel('Laufzeit {\itt}_{comp}')
legend('DFT ideal', 'FFT ideal')

figure
plot(2.^(1:N), ft_ML_time)
xlabel('Laufzeit {\itt}_{run}')
title('Matlab FFT')


    