clear all; clc; close all
x = 0:0.005:10;
y = x.*log10(x);
plot(x, y, '.r');


hold on;
y2 = x.*log(x);
plot(x, y2, '.b');


hold on;
b=2;
y3 = log(1+ exp(b*x));
plot(x, y3, '.g');


hold on;
b=-2;
y4 = log(1+ exp(b*x));
plot(x, y4, '.y');

hold off;
[x5,y5]= meshgrid(0:0.005:10);
z = 2*x5.*x5 - 3*x5.*y5 + 5*y5.*y5;
mesh(z);