u = linspace(-1, 1);
v = linspace(0, 3);
[U, V] = meshgrid(u, v);
mesh(U.*V.^2, U, sin(U.*V))
