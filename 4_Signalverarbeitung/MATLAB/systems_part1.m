close all
clear all
clc

% Parameters from the excercise question
f_s = 1e6;
N = 2^11;
f_base = 2e3;

% Build corresponding time vector
t = (0:N-1)./f_s;
t = t(:); % make it a column vector

% Create rectangular test signal
u_test = sign(sin(2*pi*f_base*t));

% Apply own sys() function to test signal
b_system1 = [0.1367, 0.1367];
a_system1 = [1 -0.7265];
u_out_system1 = sys(b_system1, a_system1, u_test);

% Ensure sys is working correctly (compare to MATLAB's implementation)
u_out_check = filter(b_system1, a_system1, u_test);
if any(u_out_system1 - u_out_check > 1e-15) % numerical errors are possible
    disp('Oops. sys() does not do what it''s supposed to do.');
end

% Visualize the signal
figure
plot(t.*1e3, u_test);
hold on
plot(t.*1e3, u_out_system1);
xlim([0, 2]);
ylim([-1.1 1.1]);
xlabel('Time {\itt} / ms');
ylabel('Voltage {\itu} / V');

% Do the same thing for the second set of parameters
b_system2 = [0.8633, -0.8633];
a_system2 = [1 -0.7265];
u_out_system2 = sys(b_system2, a_system2, u_test);

figure
plot(t.*1e3, u_test);
hold on
plot(t.*1e3, u_out_system2);
xlim([0, 2]);
ylim([-1.1 1.1]);
xlabel('Time {\itt} / ms');
ylabel('Voltage {\itu} / V');
