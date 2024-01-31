clear all; clc; close all
h = 0.001;
X = 0:h:10;
f = X.*log10(X);
Y = diff(f)/h;
Z = diff(Y)/h;
plot(X(:,1:length(Y)),Y,'r',X,f,'b', X(:,1:length(Z)),Z,'k')
% red   - first order derivative
% blue  - function
% black - second order derivative

hold on;
f = X.*log(X);
Y = diff(f)/h;
Z = diff(Y)/h;
plot(X(:,1:length(Y)),Y,'r',X,f,'b', X(:,1:length(Z)),Z,'k');