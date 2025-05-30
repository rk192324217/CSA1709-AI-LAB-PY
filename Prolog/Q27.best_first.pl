% Heuristic: straight-line distance to Bucharest
h(arad, 366).
h(bucharest, 0).
h(craiova, 160).
h(dobreta, 242).
h(eforie, 161).
h(fagaras, 178).
h(giurgiu, 77).
h(hirsova, 151).
h(iasi, 226).
h(lugoj, 244).
h(mehadia, 241).
h(neamt, 234).
h(oradea, 380).
h(pitesti, 98).
h(rimnicu_vilcea, 193).
h(sibiu, 253).
h(timisoara, 329).
h(urziceni, 80).
h(vaslui, 199).
h(zerind, 374).

% Graph edges
edge(arad, zerind, 75).
edge(arad, sibiu, 140).
edge(arad, timisoara, 118).
edge(bucharest, pitesti, 101).
edge(bucharest, fagaras, 211).
edge(bucharest, giurgiu, 90).
edge(bucharest, urziceni, 85).
edge(craiova, dobreta, 120).
edge(craiova, rimnicu_vilcea, 146).
edge(craiova, pitesti, 138).
edge(dobreta, mehadia, 75).
edge(eforie, hirsova, 86).
edge(fagaras, sibiu, 99).
edge(hirsova, urziceni, 98).
edge(iasi, neamt, 87).
edge(iasi, vaslui, 92).
edge(lugoj, mehadia, 70).
edge(lugoj, timisoara, 111).
edge(oradea, zerind, 71).
edge(oradea, sibiu, 151).
edge(pitesti, rimnicu_vilcea, 97).
edge(rimnicu_vilcea, sibiu, 80).
edge(urziceni, vaslui, 142).

best_first(Start, Goal) :-
    best_first_search(Start, Goal, [Start], Path),
    reverse(Path, ReversedPath),
    write('Path: '), write(ReversedPath), nl.

best_first_search(Goal, Goal, Visited, Visited).
best_first_search(Current, Goal, Visited, Path) :-
    h(Current, HValue),
    write('Exploring: '), write(Current), write(' (h='), write(HValue), write(')'), nl,
    edge(Current, Next, _),
    \+ member(Next, Visited),
    best_first_search(Next, Goal, [Next|Visited], Path).