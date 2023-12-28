function odeRK()
    plotsoln();
    rnge = [1, 1.5];
    y0 = 1;
    [X, Y] = RKMethod(@ode1, y0, rnge);
    hold on; plot(X, Y, '*r');
end

function [X, Y] = RKMethod(dydx, y0, xspan)
    X = xspan(1):0.01:xspan(2);
    Y = zeros(size(X));
    Y(1) = y0;
    
    for i = 1:length(X)-1
        % 
        k1 = 0.01 * dydx(X(i), Y(i));
        k2 = 0.01 * dydx(X(i) + 0.01/2, Y(i) + k1/2);
        k3 = 0.01 * dydx(X(i) + 0.01/2, Y(i) + k2/2);
        k4 = 0.01 * dydx(X(i) + 0.01, Y(i) + k3);
        
        Y(i+1) = Y(i) + (k1 + 2*k2 + 2*k3 + k4)/6;
    end
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