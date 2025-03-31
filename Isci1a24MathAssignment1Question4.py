from jedi.api.helpers import infer


def tomato(x):
    if x < 0 or x > 1:
        return "Error!!"
    a = 0
    n = 0
    error_bound = 1
    while error_bound > 0.0001:
        approx = ((-1) ** n * x ** (2 * n + 1)) / (2 * n + 1)
        a += approx
        error_bound = x ** (2 * n + 3) / (2 * n + 3)
        n += 1
    return (a, n, error_bound)
x = float(input("enter your number"))
print(tomato(x))
