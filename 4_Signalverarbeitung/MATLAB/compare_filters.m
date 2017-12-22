close all
clear all
clc

% Parameters from exercise question
f_s = 1e6; % sampling frequency / Hz
N = 5; % filter order
f_c = 10e3; % cutoff frequency / Hz
atten = 40; % stopband attenuation
ripple = 3; % passband ripple

f_Nyq = f_s/2;

% Design filters
[b_butter, a_butter] = butter(N, f_c/f_Nyq);
[b_cheby1, a_cheby1] = cheby1(N, ripple, f_c/f_Nyq);
[b_cheby2, a_cheby2] = cheby2(N, atten, f_c/f_Nyq);
[b_ellip, a_ellip] = ellip(N, ripple, atten, f_c/f_Nyq);

% Calculate transfer functions
f = 0.1*f_c : 10 : 10*f_c;
G_butter = freqz(b_butter, a_butter, f, f_s);
G_cheby1 = freqz(b_cheby1, a_cheby1, f, f_s);
G_cheby2 = freqz(b_cheby2, a_cheby2, f, f_s);
G_ellip = freqz(b_ellip, a_ellip, f, f_s);

% Calculate transfer function magnitude in dB
G_butter_db = 20*log10(abs(G_butter));
G_cheby1_db = 20*log10(abs(G_cheby1));
G_cheby2_db = 20*log10(abs(G_cheby2));
G_ellip_db = 20*log10(abs(G_ellip));

% Draw plots
figure
semilogx(f, G_butter_db);
hold on
semilogx(f, G_cheby1_db);
semilogx(f, G_cheby2_db);
semilogx(f, G_ellip_db);
semilogx(f, -3*ones(size(f)), '--');
semilogx(f, -1*atten*ones(size(f)), '--');
xlim([0.1 10] .* f_c); % two decades around f_th
ylim([-2*atten 6]); % dynamic selection w.r.t. desired stopband attenuation
xlabel('Frequency {\itf} / Hz');
ylabel('Transfer Function Magnitude |{\itG}(j\omega)| / dB');
grid on
legend('Butter', 'Cheby1', 'Cheby2', 'Ellip', '-3 dB threshold', ...
       'Stopband threshold', 'Location', 'southwest');

% Find transition band
f_tr_butter = f(G_butter_db < -3 & G_butter_db > -40);
f_tr_cheby1 = f(G_cheby1_db < -3 & G_cheby1_db > -40);
f_tr_cheby2 = f(G_cheby2_db < -3 & G_cheby2_db > -40);
f_tr_ellip = f(G_ellip_db < -3 & G_ellip_db > -40);

% Output transition band properties
fprintf('Transition Bands:\n');
fprintf('Butter:\t %.1f to %.1f kHz (width: %.1f kHz)\n', ...
        f_tr_butter(1)/1e3, f_tr_butter(end)/1e3, ...
        (f_tr_butter(end)-f_tr_butter(1))/1e3);
fprintf('Cheby1:\t %.1f to %.1f kHz (width: %.1f kHz)\n', ...
        f_tr_cheby1(1)/1e3, f_tr_cheby1(end)/1e3, ...
        (f_tr_cheby1(end)-f_tr_cheby1(1))/1e3);
fprintf('Cheby2:\t %.1f to %.1f kHz (width: %.1f kHz)\n', ...
        f_tr_cheby2(1)/1e3, f_tr_cheby2(end)/1e3, ...
        (f_tr_cheby2(end)-f_tr_cheby2(1))/1e3);
fprintf('Ellip:\t %.1f to %.1f kHz (width: %.1f kHz)\n', ...
        f_tr_ellip(1)/1e3, f_tr_ellip(end)/1e3, ...
        (f_tr_ellip(end)-f_tr_ellip(1))/1e3);
