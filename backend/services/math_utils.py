from sympy import symbols, Eq, solve

def solve_equation():
    x, y = symbols('x y')
    equation = Eq(x**2 + y**2, 1)
    solution = solve(equation, y)
    return solution
