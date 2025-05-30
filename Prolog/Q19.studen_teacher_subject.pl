% Facts: subject_code(Subject, Code)
subject_code(math, 101).
subject_code(physics, 102).
subject_code(chemistry, 103).

% Facts: teacher(Teacher, Subject)
teacher(dr_smith, math).
teacher(dr_jones, physics).
teacher(dr_lee, chemistry).

% Facts: student(Student, Subject)
student(alice, math).
student(bob, physics).
student(charlie, chemistry).
student(alice, physics).

% Query examples:
% Find all teachers: ?- teacher(Teacher, _).
% Find students taking math: ?- student(Student, math).
% Find subjects taught by dr_jones: ?- teacher(dr_jones, Subject).