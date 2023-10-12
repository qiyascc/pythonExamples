Y = (lambda f: (lambda x: x(x))(lambda y: f(lambda *args: y(y)(*args))))
factorial = Y(lambda f: lambda n: 1 if n == 0 else n * f(n-1))

n = 5
print(factorial(n))
