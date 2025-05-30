% Knowledge base
clause(flies(X), [bird(X), not(abnormal(X))]).
clause(bird(X), [penguin(X)]).
clause(abnormal(X), [penguin(X)]).
fact(penguin(tweety)).

% Backward chaining engine
prove(Goal) :-
    fact(Goal).

prove(Goal) :-
    clause(Goal, Body),
    prove_all(Body).

prove_all([]).
prove_all([H|T]) :-
    prove(H),
    prove_all(T).

% Query:
% ?- prove(flies(tweety)).  % Returns false
% ?- prove(bird(tweety)).   % Returns true