% Base case: sum of 1 is 1
sum_to_n(1, 1).

% Recursive case: sum(N, Total) = Total is sum of 1 to N
sum_to_n(N, Total) :-
    N > 1,
    Prev is N - 1,
    sum_to_n(Prev, SumPrev),
    Total is SumPrev + N.

% Helper predicate for easy querying
sum_up_to(N) :-
    sum_to_n(N, Total),
    format('Sum of integers from 1 to ~d is ~d', [N, Total]).