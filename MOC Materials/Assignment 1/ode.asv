function ode()
    clear all; clc; close all

    rnge = 1:0.001:1.5;
    y = rnge.*sqrt(1-2*log(rnge));
    plot(rnge, y, '.b');
    odedsolve();
end

function odedsolve()
    syms y(x);
    diffeq = diff(y) == (y.^2 - x.^2)/(x*y);
    ivp = y(1) == 1;
    soln = dsolve(diffeq, ivp);
    x = 1:0.005:1.5;
    y = subs(soln(1));
    hold on; plot(x, y, '.r');
end

function odeode45()
    xrange = [1 1.5];
    y0 = 1;
    [x, y] = ode45()

end