function [coeff] = fftMSMP(signal)
%fftMSMP calculates the DFT using the FFT algorithm

signal = signal(:); % make sure signal is a collum vector
N = length(signal);

if N == 1   % base case
    coeff = signal;
else    
    % transform the halfed signals recursively
    signal_even = signal(1:2:end);
    signal_odd = signal(2:2:end);
    transfEven = fftMSMP(signal_even);
    transfOdd = fftMSMP(signal_odd);
    
    % combine divided dfts
    k = 0:N/2-1;
    coeff(k+1) = transfEven+transfOdd.*exp(-i*2*pi/N.*k);
    % symmetry
    coeff(N/2+1+k) = transfEven-transfOdd.*exp(-i*2*pi/N.*k);
end
end

