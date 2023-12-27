function odeode45()
    plotsoln();
    xrange = [1 1.5];
    y0 = 1;
    [x, y] = ode45(@ode1, xrange, y0);
    hold on; plot(x, y, '*r')
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