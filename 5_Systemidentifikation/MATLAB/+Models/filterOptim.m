function output = filterOptim(sigIn, cutoffFrequ, order)
% Forward model function (a low-pass filter).
%
% Args:
%     sig_in: Input signal
%     cutoff_frequ: Normalized cutoff frequency.
%     order: Order of the filter.
%
% Returns:
%     Output signal of the model.

    % Limit cut-off frequency values 0< .. <1
    cutoffFrequ(cutoffFrequ > 1) = 1 - eps;
    cutoffFrequ(cutoffFrequ < 0) = eps;
 
    [b, a] = butter(order, cutoffFrequ);    
    output = filter(b, a, sigIn);
end
