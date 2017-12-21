function u_out = sys(b, a, u_in)
%SYS Calculate the response u_out for a given input u_in of a system described
%by the transfer function coefficients b and a.

% Initialize output vector (same length as input)
u_out = zeros(size(u_in));

% For all elements...
for n = 1:length(u_in)
    % ...create a temporary accumulation variable
    tmp = 0;

    % For all elements in b...
    for p = 1:length(b)
        if p <=n % ensure positive indexing in u_in
            % add the current feed-forward term
            tmp = tmp + b(p) * u_in(n-p+1);
        end
    end

    % For all elements in a, except the first one...
    for q = 2:length(a)
        if q <= n % ensure positive indexing in u_in
            % subtract the current feed-back term
            tmp = tmp - a(q) * u_out(n-q+1);
        end
    end

    % Apply the accumulated value to the output
    u_out(n) = tmp;
end

% Apply the gain factor to the whole output vector
u_out = u_out ./ a(1);

end
