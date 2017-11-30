clear all
close all
clc

load('signals.mat')     % load y_send, y_rec and sampl_freq
t = (0:length(y_rec)-1)./sampl_freq;
figure
plot(t*1e6, y_send, 'LineWidth', 2)
hold on
plot(t*1e6, y_rec, 'r', 'LineWidth', 2)
xlabel('Time {\itt} / µs')
ylim([-1.2, 1.2])
legend('sending signal', 'received signal')

% calculate the envelope(the envelope of a signal y can be calulated by 
% the absolute value of its analytic signal) 
y_rec_env = abs(hilbert(y_rec));
y_send_env = abs(hilbert(y_send));

hold on
plot(t*1e6, y_send_env, 'b--')
hold on
plot(t*1e6, y_rec_env, 'r--')

% correlate the envelopes
[correlation_ana, lag] = xcorr(y_rec_env, y_send_env);

figure
plot(lag/sampl_freq, correlation_ana)
xlabel('Time \tau / s')

% find peaks
[pks,locs] = findpeaks(correlation_ana);
% sort paeks in descending order
peaks_sorted = flipud(sortrows([pks, locs]));

% plot largest peaks
hold on
stem(lag(peaks_sorted(1:3, 2))/sampl_freq, correlation_ana(peaks_sorted(1:3, 2)), 'r')

% calculate t_0 and t_1
t_0 = lag(peaks_sorted(1, 2))/sampl_freq;
t_1 = lag(peaks_sorted(2, 2))/sampl_freq;

delta_t = t_1-t_0;

l = 16.9e-3;
D = 6e-3;
% calculate longitudinal and transversal wave velocities
c_l = l/t_0;
c_t = c_l/(sqrt(1+(delta_t*c_l/D)^2));

disp(['Longitudinalwellengeschwindigkeit: ', num2str(c_l), ' m/s'])
disp(['Transversalwellengeschwindigkeit: ', num2str(c_t), ' m/s'])