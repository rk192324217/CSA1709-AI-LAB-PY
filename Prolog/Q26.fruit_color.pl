fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grape, purple).
fruit_color(orange, orange).
fruit_color(blueberry, blue).

% Query examples:
% ?- fruit_color(Fruit, Color).  % Backtracks through all possibilities
% ?- fruit_color(apple, WhatColor).
% ?- findall(Color, fruit_color(_, Color), AllColors).