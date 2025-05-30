can_fly(penguin, no).
can_fly(sparrow, yes).
can_fly(ostrich, no).
can_fly(eagle, yes).
can_fly(kiwi, no).

% Query examples:
% ?- can_fly(sparrow, Answer).  % Returns: Answer = yes
% ?- can_fly(penguin, no).      % Returns: true
% ?- findall(Bird, can_fly(Bird, yes), FlyingBirds).