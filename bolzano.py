


from sympy import symbols, Eq, solve
x = symbols('x')
equation =  Eq(((x*x*x)-x), 1)

A = solve(equation,(x))
print(A)

