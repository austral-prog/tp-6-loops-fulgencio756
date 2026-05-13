# Replace the "ANSWER HERE" for your answer

def sum_to_n(n):
    """
    Retorna la suma de todos los enteros desde 1 hasta n (inclusive).
    Si n <= 0, retorna 0.

    Ejemplo: sum_to_n(5) -> 15  (1+2+3+4+5)
    """
    total = 0
    for numero in range(1, n+1):
        total += numero
    return total



def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def sum_evens(n):
    total = 0
    for i in range(2, n + 1, 2):
        total += i
    return total

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

