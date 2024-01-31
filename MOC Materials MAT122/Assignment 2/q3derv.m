clear all; clc; close all
h = 0.001;
rnge = 0:h:10;
syms X Y
z = 2*X.*X - 3*X.*Y + 5*Y.*Y;
dzdx = diff(z, X);
dzdy = diff(z, Y);
dzdx2 = diff(dzdx, X);
dzdy2 = diff(dzdy, Y);
dzdxdy = diff(dzdx, Y);
disp(double(dzdx(5, 10)))
% plot(X(:,1:length(dzdx)),dzdx,'r',X,z,'b', X(:,1:length(dzdy)),dzdy,'k')
% red   - first order derivative
% blue  - function
% black - second order derivative