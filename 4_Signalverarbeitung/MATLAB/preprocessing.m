close all
clear all
clc

% Load measurement data
load('preprocessing_data.mat');

% Preserve original signal for later comparison
u_orig = u;

% Detrend & find envelope
u = detrend(u);
u_env = abs(hilbert(u));

% Visually compare original, detrended signal and envelope
figure
plot(t.*1e3, u_orig);
hold all
plot(t.*1e3, u);
plot(t.*1e3, u_env);
legend('Original', 'Detrended', 'Envelope');
xlabel('Time {\itt} / ms');
ylabel('Voltage {\itu} / V');

% Remove irrelevant data parts
% Note: The limits can be determined by finding the section of the envelope
%       that is less noisy.
u(t<1.05e-4 | t>1.4e-4) = [];
t(t<1.05e-4 | t>1.4e-4) = [];

% Determine amplitude...
% ...either via envelope (larger error)
u_hat_1 = mean(abs(hilbert(u)));

% ...or via findpeaks
% Note: MinPeakDistance is required so that small noise-related peaks near the
%       local minima are not found.
[u_max, idx_max] = findpeaks(u, 'MinPeakDistance', 30);
u_hat_2 = mean(u_max);

% Visualize the relevant signal part and the detected amplitudes
figure
plot(t.*1e3, u);
hold all
plot(t.*1e3, ones(size(u)) .* u_hat_1);
plot(t.*1e3, ones(size(u)) .* u_hat_2);
legend('Extracted signal', 'Amplitude (via envelope)', ...
       'Amplitude (via findpeaks)');
xlabel('Time {\itt} / ms');
ylabel('Voltage {\itu} / V');

% Determine signal frequency
% Note: This solution is in time domain, but frequency domain also works well.
delta_t = mean(diff(t(idx_max)));
f_sig = 1/delta_t;

% Determine phase offset
phi = phase_compensation(t, u, f_sig);

% Compare simulated and measured signal
u_sim = u_hat_2 .* sin(2*pi*f_sig*(t) - phi);

figure
plot(t.*1e3, u);
hold all
plot(t.*1e3, u_sim);
legend('Measurement', 'Simulation');
xlabel('Time {\itt} / ms');
ylabel('Voltage {\itu} / V');
