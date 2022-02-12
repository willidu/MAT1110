t = linspace(-2, 2, 31);
[x, y] = meshgrid(t);
u = -y./(x.^2+y.^2);
v = x./(x.^2+y.^2);
quiver(x, y, u, v)
hold on
streamline(x, y, u, v, 1, 0)
axis equal
