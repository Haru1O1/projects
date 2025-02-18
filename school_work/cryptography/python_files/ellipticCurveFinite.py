from sympy import symbols

def main():
    # Define symbols
    x, y = symbols('x y')

    # Curve parameters
    a = 3
    b = 2
    r = 7  # Prime modulus

    # Define the curve equation
    curve_equation = y**2 - x**3 - a*x - b

    # Print the curve equation
    print("Curve equation:", curve_equation)

    # Iterate over the finite field and find points satisfying the curve equation
    points = []
    for x_val in range(r):
        for y_val in range(r):
            if curve_equation.subs({x: x_val, y: y_val}) % r == 0:
                points.append((x_val, y_val))

    # Print the points satisfying the curve equation
    print("Points on the curve:")
    for point in points:
        print(point)

if __name__ == "__main__":
    main()