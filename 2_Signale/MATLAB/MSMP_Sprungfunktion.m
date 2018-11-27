x = 1:0.5:8;
M = 2;
y = sprung_schleife(x, 4);
stem(x, y)

function y = sprung_heaviside(x, M)
    y = heaviside(x-M);
    y(x==M) = 1;
end

function y = sprung_sign(x, M)
    y = sign(x-M);
    index = find(x==M);
    disp(index)
    y(x==M)=1;
    y = (1.+y)/2;
end

function y = sprung_indexing(x, M)
    y = ones(size(x));
    y(x<M)=0;
end

function y = sprung_schleife(x, M)
    y = ones(1,length(x));
    for idx=1:length(x)
       if x(idx)<M
           y(idx)=0;
       end
    end
end