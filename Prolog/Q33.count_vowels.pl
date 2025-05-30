vowel(a). vowel(e). vowel(i). vowel(o). vowel(u).

count_vowels([], 0).
count_vowels([H|T], Count) :-
    (vowel(H) -> 
        count_vowels(T, SubCount), Count is SubCount + 1
        ; count_vowels(T, Count).

% Helper predicate for string input
string_vowels(String, Count) :-
    string_lower(String, Lower),
    string_chars(Lower, Chars),
    count_vowels(Chars, Count).

% Query:
% ?- string_vowels("Artificial Intelligence", Count).
% Count = 9