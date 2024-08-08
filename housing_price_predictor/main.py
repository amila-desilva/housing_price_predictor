def fibonacci(n):
    """
    Calculate the nth Fibonacci number. This method represents the 'dummy' method instructed by the mentor. 

    Args:
        n (int): The position in the Fibonacci sequence.

    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b 


# main function for printing result for demostration
if __name__ == "__main__":
    n = 10  # Change this value to test different inputs
    print(f"Fibonacci number at position {n} is {fibonacci(n)}")