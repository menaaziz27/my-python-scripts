def n_sided_shape(n):
	lst = "circle semi-circle triangle square pentagon hexagon heptagon octagon nonagon decagon".split(" ")
	return lst[n - 1]

print(n_sided_shape(1))
