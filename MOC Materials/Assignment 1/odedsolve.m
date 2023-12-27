function odedsolve()
    plotsoln();
    syms y(x) x;
    diffeq = diff(y) == ode1(x, y);
    ivp = y(1) == 1;
    soln = dsolve(diffeq, ivp);
    x = 1:0.01:1.5;
    y = subs(soln(1));
    hold on; plot(x, y, '*r');
end

function dydx = ode1(x, y)
    dydx = (y.^2 - x.^2)/(x*y);
end

function plotsoln()
    clear all; clc; close all

    rnge = 1:0.001:1.5;
    y = rnge.*sqrt(1-2*log(rnge));
    plot(rnge, y, '.b');
end