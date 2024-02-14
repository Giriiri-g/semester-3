A = [1 2 3; 2 4 6; 7 8 9];
b = [1; 1; 1];

x = zeros(3, 1);
r = b;
d = r;
threshold = 0.0001;
xprev = x;
iteration = 1;
while true
    a = (r'*r)/(d'*A*d);
    xprev = x;
    x = x + a*d;
    if abs(sum(xprev) - sum(x)) < threshold
        break
    end
    rk_1 = r;
    r = r - a*A*d;
    beta = (r'*r)/(rk_1'*rk_1);
    d = r + beta*d;
    
    % Debugging output
    disp(['Iteration: ', num2str(iteration)]);
    disp(['a: ', num2str(a)]);
    disp(['x: ', mat2str(x)]);
    disp(['r: ', mat2str(r)]);
    disp(['beta: ', num2str(beta)]);
    disp(['d: ', mat2str(d)]);
    
    iteration = iteration + 1;
end

disp(x);
