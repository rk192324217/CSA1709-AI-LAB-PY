diet(diabetes, ['Low sugar', 'High fiber', 'Whole grains']).
diet(hypertension, ['Low sodium', 'Fruits', 'Vegetables']).
diet(obesity, ['Portion control', 'Lean proteins', 'Low fat']).
diet(anemia, ['Iron-rich foods', 'Vitamin C', 'Leafy greens']).

suggest_diet(Disease) :-
    diet(Disease, Recommendations),
    write('For '), write(Disease), write(' recommended diet:'), nl,
    print_list(Recommendations).

print_list([]).
print_list([H|T]) :- write('- '), write(H), nl, print_list(T).