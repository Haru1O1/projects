def inverse_exist(a, m):
    for i in range(1, m):
        if (a*i) % m == 1:
            return i
    return None

def is_quadratic_residue(a, p):
    return pow(a, (p - 1) // 2, p) == 1

def elliptic_curve(x, p):
    # elliptic curve x^e + fx + g
    e = 3
    f = 3
    g = 2
   
    a = x**e + f*x + g

    return a, a % p

def line(x, m, b, p):
    return (m*x + b) % p

def solve_intersection_points(p, m, b):
    intersection_points = []
    if inverse_exist(m, b) is None:
        print("no inverse")
        return intersection_points
    
    for x in range(p):
        a, y_square = elliptic_curve(x, p)
        if is_quadratic_residue(y_square, p):
            y = pow(y_square, (p + 1) // 4, p)
            line_y = line(x, m, b, p)
            if line_y == y:
                intersection_points.append((x, y))
            if line_y == p - y:
                intersection_points.append((x, p - y))
        print(f"x: {x}, y: {y}, y_square: {y_square}, line(x, m, b, p): {line(x, m, b, p)}")
    return intersection_points

def main():
    # y = mx + b mod p
    p = 7
    m = 4
    b = 3
    intersection_points = solve_intersection_points(p, m, b)
    print("Intersection points:", intersection_points)

if __name__ == "__main__":
    main()