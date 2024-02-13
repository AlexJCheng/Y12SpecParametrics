import sympy as sp

def parametric_to_cartesian(x_t, y_t, t):
    # Solve one of the parametric equations for t
    t_exprs = sp.solve(sp.Eq(x_t, x), t)
    print(t_exprs)
    # Substitute each solution into the other parametric equation
    cartesian_eqs = [sp.Eq(y_t.subs(t, t_expr), y) for t_expr in t_exprs]

    return cartesian_eqs

# Define the parameter and variables
t, x, y = sp.symbols('t x y')

# Define the parametric equations
x_t = sp.cos(t)
y_t = sp.sin(t)

# Convert to Cartesian
cartesian_eqs = parametric_to_cartesian(x_t, y_t, t)

# Print the Cartesian equations
for eq in cartesian_eqs:
    print(eq)
