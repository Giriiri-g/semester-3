function age = calcAge(p)
    hl = 5730;  % Half-life of C14 in years
    fr = 1 - p / 100;
    dc = log(2) / hl;
    age = -1 / dc * log(fr);
    fprintf('Predicted age: %.2f years\n', age);
end