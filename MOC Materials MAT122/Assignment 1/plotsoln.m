function plotsoln()
    clear all; clc; close all

    rnge = 1:0.001:1.5;
    %y = rnge.*sqrt(1-2*log(rnge));                                    % a)
    %y = (1 - exp(-rnge.^2))/2;                                        % b)
    %y= -rnge.*exp(-rnge)/2 + exp(-rnge)/4 - exp(-3.*rnge)/4;          % d)
    plot(rnge, y, '.b');
end