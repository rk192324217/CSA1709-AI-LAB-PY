% Knowledge base
rule(1, [bird, lays_eggs], penguin).
rule(2, [penguin], bird).
rule(3, [bird, can_fly], flying_animal).

% Forward chaining engine
forward_chain(Facts, NewFacts) :-
    findall(NewFact, 
            (rule(_, Conditions, NewFact),
            \+ member(NewFact, Facts),
            subset(Conditions, Facts)),
    NewFacts.

% Query helper
solve(Query) :-
    forward_chain([], InitialFacts),
    (member(Query, InitialFacts) -> 
        write('Derived: '), write(Query), nl
        ; write('Cannot derive '), write(Query)).

% Example usage:
% ?- solve(flying_animal).