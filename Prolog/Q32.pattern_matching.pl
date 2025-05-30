% Base case: empty pattern matches empty string
match([], []).

% Wildcard matches any single character
match(['_'|Ptail], [_|Stail]) :- match(Ptail, Stail).

% Character match
match([C|Ptail], [C|Stail]) :- match(Ptail, Stail).

% Star matches zero or more characters
match(['*'|Ptail], String) :- match(Ptail, String).
match(['*'|Ptail], [_|Stail]) :- match(['*'|Ptail], Stail).

% Query examples:
% ?- match([a, b, c], [a, b, c]).  % true
% ?- match([a, '*', c], [a, b, b, c]).  % true
% ?- match(['_', b, '*'], [x, b, c, d]).  % true