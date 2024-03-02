clear all;
% very large matrix
% For conjugate gradient to converge to a valid solution, it is necessary for $A$ to be square,
% symmetric positive definite matrix
dim = 2000; % size of the matrix
vec = -1*ones(dim-1,1); % create a vector
A = 4*eye(dim) + diag(vec,1)+diag(vec,-1); % create matrix
A(1,1) = 100; % change Matrix to get an illconditioned matrix
% compute Condition matrix
cond(A)
%define righthandside of Ax=b
b = ones(dim,1);
% set maximal iteration and Tolerances 
maxiter = 1000;
tol = 10e-6; % .000001
% set initial vector
u_0 = zeros(dim,1);
% run your implemented cg method
[u_cg, iter] = cg(A, b, maxiter, tol, u_0);
% compute norm of the difference of the solution in every iteration with the final solution
norm_diff_cg = zeros(iter, 1);
for i = 1:iter
    norm_diff_cg(i) = norm(u_cg(1:i) - u_cg);
end
% run your implemented pcg
[u_pcg, iter_pcg] = p_cg(A,b,maxiter,tol,u_0);
% compute norm of the difference of the solution in every iteration with the final solution
norm_diff_pcg = zeros(iter_pcg, 1);
for i = 1:iter_pcg
    norm_diff_pcg(i) = norm(u_pcg(1:i) - u_pcg);
end
% visualize the norm of the difference
figure;
semilogy(1:iter, norm_diff_cg);
xlabel('Iteration');
ylabel('Norm of the Difference');
title('Norm of the Difference for CG');
figure;
semilogy(1:iter_pcg, norm_diff_pcg);
xlabel('Iteration');
ylabel('Norm of the Difference');
title('Norm of the Difference for PCG');