% Facts: name_dob(Name, DateOfBirth)
name_dob(john, date(1990, 5, 15)).
name_dob(sarah, date(1985, 12, 3)).
name_dob(mike, date(1995, 8, 22)).
name_dob(lisa, date(1988, 3, 30)).

% Query examples:
% Find all names: ?- name_dob(Name, _).
% Find DOB for a name: ?- name_dob(john, DOB).
% Find people born after 1990: ?- name_dob(Name, date(Year, _, _)), Year > 1990.