close all
clear all
clc

% Load given test signal
load('ma_filtering.mat');

% Calculate sampling frequency
% Note: All values of diff(t) should be equal (equidistant sampling!), but
%       there can be small numerical errors - hence the mean().
f_s = round(1/mean(diff(t)));

%% PART 1 %%
% Define filter coefficients for order N = 2
N = 2;
b_2 = ones(N, 1) / N;

% Apply the filter
u_out_2 = filter(b_2, 1, u); % a = 1 because of FIR filter

% Plot the results
figure
plot(t.*1e3, u);
hold on
plot(t.*1e3, u_out_2);
xlim([0 0.2]);
ylim([-1.1 1.1]);
xlabel('Time {\itt} / ms');
ylabel('Voltage {\itu} / V');
legend('Unfiltered', '{\itN} = 2');

%% PART 2 %%
% Define and apply some more filters with higher order
b_5 = ones(5, 1) / 5;
b_10 = ones(10, 1) / 10;
u_out_5 = filter(b_5, 1, u);
u_out_10 = filter(b_10, 1, u);

% Plot the results
figure
plot(t.*1e3, u);
hold on
plot(t.*1e3, u_out_2);
plot(t.*1e3, u_out_5);
plot(t.*1e3, u_out_10);
xlim([0 0.2]);
ylim([-1.1 1.1]);
xlabel('Time {\itt} / ms');
ylabel('Voltage {\itu} / V');
legend('Unfiltered', '{\itN} = 2', '{\itN} = 5', '{\itN} = 10');

% Problem, visible esp. for N = 10: phase offset!

% Filter again using filtfilt and N = 10
u_filtfilt = filtfilt(b_10, 1, u);

figure
plot(t.*1e3, u);
hold on
plot(t.*1e3, u_filtfilt);
plot(t.*1e3, u_out_10);
xlim([0 0.2]);
ylim([-1.1 1.1]);
xlabel('Time {\itt} / ms');
ylabel('Voltage {\itu} / V');
legend('Unfiltered', '{\itN} = 10 (filtfilt)', '{\itN} = 10');

% Comparison is not fair: filtfilt-signal is much smoother than the other.
% Why? filtfilt performs double filtering, thus doubling the effective filter
% order! For a fair comparison, compare filtfilt with N = 10 to filter with
% N = 20.

b_20 = ones(20, 1) / 20;
u_out_20 = filter(b_20, 1, u);

figure
plot(t.*1e3, u);
hold on
plot(t.*1e3, u_filtfilt);
plot(t.*1e3, u_out_20);
xlim([0 0.2]);
ylim([-1.1 1.1]);
xlabel('Time {\itt} / ms');
ylabel('Voltage {\itu} / V');
legend('Unfiltered', '{\itN} = 10 (filtfilt)', '{\itN} = 20');
