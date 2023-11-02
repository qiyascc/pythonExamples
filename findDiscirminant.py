roots = (lambda a, b, c: (-b / (2 * a),) if b**2 == 4*a*c and a != 0 else (None,) if b**2 < 4*a*c or (a == 0 and b == 0) else (-c / b,) if a == 0 else ((-b + (b**2 - 4*a*c)**0.5) / (2*a), (-b - (b**2 - 4*a*c)**0.5) / (2*a)))

a, b, c = 0, 1, -3
x = roots(a, b, c)

if x[0] is None:
    print("No solution")
elif len(x) == 1:
    print("D: 0" if a != 0 else "")
    print("x:", x[0])
else:
    discriminant = (b**2 - 4 * a * c)**0.5
    print("D:", discriminant)
    print("x1:", x[0])
    print("x2:", x[1])