import sympy as sp

def simulate_custom_model(equation, parameters):
    t = sp.symbols('t')
    y = sp.Function('y')
    eq = sp.Eq(sp.diff(y(t), t), sp.sympify(equation))
    solution = sp.dsolve(eq, y(t))
    return solution
