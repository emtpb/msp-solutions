clear all
close all
clc

%% PART 1
sampl_freq = 50e6;      % sampling frequency

% signal generation
f_center = 1e6;         % center frequency
bandwidth = 0.6;        % relative bandwidth
tc = gauspuls('cutoff', f_center, bandwidth, [], -40);
t_center = -tc : 1/sampl_freq : tc;

y = gauspuls(t_center, f_center, bandwidth);
t = (0:length(y)-1)./sampl_freq;

plot(t*1e6, y)
xlabel('Time {\itt} / µs')
title(['Time domain. f_{sampl} = ', num2str(sampl_freq/1e6), ' MHz; N = ', num2str(length(y))])

delta_f = sampl_freq/length(y);
f = -sampl_freq/2:delta_f:sampl_freq/2-delta_f;

figure
plot(f, abs(fftshift(fft(y))));
xlabel('Frequency {\itf} / Hz')
title(['Frequency domain. f_{sampl} = ', num2str(sampl_freq/1e6), ' MHz; N = ', num2str(length(y))])

% zeropadding
number_zeros = 1000;
y_padded = [y, zeros(1, number_zeros)];
t_padded = (0:length(y_padded)-1)./sampl_freq;
figure
plot(t_padded*1e6, y_padded)
xlabel('Time {\itt} / µs')
title(['Time domain. f_{sampl} = ', num2str(sampl_freq/1e6), ' MHz; N = ', num2str(length(y_padded))])

delta_f_padded = sampl_freq/length(y_padded);
f_padded = -sampl_freq/2:delta_f_padded:sampl_freq/2-delta_f_padded;

figure
plot(f_padded, abs(fftshift(fft(y_padded))));
xlabel('Frequency {\itf} / Hz')
title(['Frequency domain. f_{sampl} = ', num2str(sampl_freq/1e6), ' MHz; N = ', num2str(length(y_padded))])

%% PART 2
% add signal with higher frequencies
c = 25;
disp(['Zusaätzliche Mittenfrequenz: ', num2str(f_center*c/1e6), ' MHz'])

y_high_freq = gauspuls(t_center, f_center*c, bandwidth/c);
y_add =y + y_high_freq;
figure
plot(t, y)
hold on
plot(t, y_high_freq, 'r')
hold on
plot(t, y_add, 'g')
xlabel('Time {\itt} / µs')
title(['Time domain. f_{sampl} = ', num2str(sampl_freq/1e6), ' MHz; N = ', num2str(length(y_add))])
legend('lower freq.', 'high freq.', 'sum')

figure
plot(f, fftshift(abs(fft(y_add))))
xlabel('Frequency {\itf} / Hz')
title(['Frequency domain. f_{sampl} = ', num2str(sampl_freq/1e6), ' MHz; N = ', num2str(length(y_add))])

y_add_padded = [y_add, zeros(1, number_zeros)];

figure
plot(f_padded, fftshift(abs(fft(y_add_padded))))
xlabel('Frequency {\itf} / Hz')
title(['Frequency domain. f_{sampl} = ', num2str(sampl_freq/1e6), ' MHz; N = ', num2str(length(y_add_padded))])






