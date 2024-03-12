% Define the function
f = @(x, y) 0.5*x.^2 - y;

% Define the constraint boundaries
x_min = 1;
x_max = sqrt(25);
y_min = (x_max - x_min)/2;
y_max = 3 - x_min/2;

% Create meshgrid for plotting the function
[X, Y] = meshgrid(x_min:0.1:x_max, y_min:0.1:y_max);

% Apply constraint x >= 1 directly by limiting the grid generation
X = X(1:max(find(X >= x_min)), :);  % Adjust to include only valid indices
Y = Y(1:max(find(X >= x_min)), :);

% Calculate the function value at each point within the valid x range
Z = f(X, Y);

% Apply the constraint (x + 2y <= 6) by setting values outside the constraint to NaN
Z(X + 2*Y > 6) = NaN;

% Apply the constraint (x^2 + y^2 <= 25) by setting values outside the constraint to NaN
Z(X.^2 + Y.^2 > 25) = NaN;

% Plot the surface
figure
surf(X, Y, Z)

% Set labels and title
xlabel('X');
ylabel('Y');
zlabel('f(x,y)');
title('Plot of (1/2)*x^2 - y constrained by x>=1, x+2y <= 6, x^2 + y^2 <= 25');

% Adjust view for better visualization
view([-45 45]);
