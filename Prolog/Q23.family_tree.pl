parent(john, mary).
parent(john, bob).
parent(mary, ann).
parent(mary, tom).
parent(bob, lisa).

male(john).
male(bob).
male(tom).
female(mary).
female(ann).
female(lisa).

grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

% Query examples:
% ?- parent(john, Child).
% ?- grandparent(john, Grandchild).
% ?- sibling(ann, tom).