function ode()
    clear all; clc; close all

    rnge = 1:0.005:1.5;
    y = rnge.*sqrt(1-2*log(rnge));
    plot(rnge, y, '.b');
end

function odedsolve()
    syms = y(x);
end