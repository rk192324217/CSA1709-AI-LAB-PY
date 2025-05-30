% Facts: planet(Name, Type, DistanceFromSunAU, Moons)
planet(mercury, terrestrial, 0.39, 0).
planet(venus, terrestrial, 0.72, 0).
planet(earth, terrestrial, 1.0, 1).
planet(mars, terrestrial, 1.52, 2).
planet(jupiter, gas_giant, 5.20, 79).
planet(saturn, gas_giant, 9.58, 82).
planet(uranus, ice_giant, 19.22, 27).
planet(neptune, ice_giant, 30.05, 14).

% Query examples:
% Find all gas giants: ?- planet(Name, gas_giant, _, _).
% Find planets with moons > 10: ?- planet(Name, _, _, Moons), Moons > 10.
% Find distance of earth: ?- planet(earth, _, Distance, _).