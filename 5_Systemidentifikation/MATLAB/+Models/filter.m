function output = filter(sigIn, cutoffFrequ, order)
% Forward model function (a low-pass filter).
%
% Args:
%     sig_in: Input signal
%     cutoff_frequ: Normalized cutoff frequency.
%     order: Order of the filter.
%
% Returns:
%     Output signal of the model.
 
    [b, a] = butter(order, cutoffFrequ);    
    output = filter(b, a, sigIn);
end
