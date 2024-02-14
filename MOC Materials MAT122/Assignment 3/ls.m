A = [1 2 3 ; 2 4 6; 7 8 9];
b = [1; 1; 1];

cvx_begin
    variable x(3);
    minimize(norm(A*x-b));
    disp(x);
cvx_end
