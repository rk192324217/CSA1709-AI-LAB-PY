symptom(fever, flu).
symptom(cough, flu).
symptom(headache, migraine).
symptom(nausea, food_poisoning).
symptom(vomiting, food_poisoning).
symptom(rash, allergy).

diagnose(Person, Disease) :-
    exhibits(Person, Symptom),
    symptom(Symptom, Disease).

exhibits(john, fever).
exhibits(john, cough).
exhibits(mary, headache).
exhibits(bob, nausea).
exhibits(bob, vomiting).

% Query:
% ?- diagnose(john, WhatDisease).
% ?- findall(D, diagnose(_, D), AllDiseases).