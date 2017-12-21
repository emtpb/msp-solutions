close all
clear all
clc

% Parameters from the excercise question
f_s = 1e6;
N = 2^11;
f_base = 2e3;

% Build correjsponding time and frequency vectors
t = (0:N-1)./f_s;
t = t(:); % make it a column vector
f = linspace(0, f_s, numel(t));
f = f(:);

% Create impulse input signal
u_in = zeros(size(t));
u_in(1) = 1; % Only the first element is 1

% Calculate the impulse responses
b_system1 = [0.1367, 0.1367];
a_system1 = [1 -0.7265];
u_out_system1 = sys(b_system1, a_system1, u_in);

b_system2 = [0.8633, -0.8633];
a_system2 = [1 -0.7265];
u_out_system2 = sys(b_system2, a_system2, u_in);

% Plot the impulse responses
figure
plot(t.*1e6, u_in, 'o');
hold on
plot(t.*1e6, u_out_system1, 'o');
plot(t.*1e6, u_out_system2, 'o');
xlim([0 15]);
ylim([-0.3 1.1]);
xlabel('Time {\itt} / µs');
ylabel('Voltage {\itu} / V');
legend('Input {\itu}_{in}', 'Output {\itu}_{out,1}', 'Output {\itu}_{out,2}');
grid on

% Calculate the transfer function
U_out_system1 = fft(u_out_system1);
U_out_system2 = fft(u_out_system2);

% Scale transfer function magnitude to dB
U_abs_system1 = 20*log10(abs(U_out_system1));
U_abs_system2 = 20*log10(abs(U_out_system2));

% Plot the transfer function (magnitude and phase)
figure
subplot(2, 1, 1);
semilogx(f(1:N/2), U_abs_system1(1:N/2)); % FFT is symmetric!
hold on
semilogx(f(1:N/2), U_abs_system2(1:N/2)); % FFT is symmetric!
semilogx(f(1:N/2), ones(N/2, 1) .* -3); % -3 dB threshold
xlim([5e2 5e5]);
ylim([-20 3]);
xlabel('Frequency {\itf} / Hz');
ylabel('|{\itG}({\itf})| / dB');
grid on
legend('System 1', 'System 2', '3 dB threshold', 'Location', 'southwest');

subplot(2, 1, 2);
semilogx(f(1:N/2), angle(U_out_system1(1:N/2))./2./pi*360); % phase in degrees
hold on
semilogx(f(1:N/2), angle(U_out_system2(1:N/2))./2./pi*360);
xlim([5e2 5e5]);
ylim([-100 100]);
xlabel('Frequency {\itf} / Hz');
ylabel('\phi({\itf}) / °');
grid on
