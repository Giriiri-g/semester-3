A = [1 2 3; 2 4 6; 7 8 9];
b = [1; 1; 1];

x = zeros(3, 1);
r = b;
d = r;
threshold = 0.005;
max_iterations = 1000;
xprev = x;
iteration = 1;
while iteration <= max_iterations
    a = (r'*r)/(d'*A*d);
    
    % Check for division by zero or very small values
    if abs(a) < eps
        disp('Skipping iteration: Division by zero or very small value.');
        iteration = iteration + 1;
        continue;
    end
    
    xprev = x;
    x = x + a*d;
    
    r_norm = norm(r); % Calculate the norm of the residual vector
    
    if r_norm < threshold
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
