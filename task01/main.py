

def caching_fibonacci():
    # Creating an empty dictionary for caching
    cache = {}
    def fibonacci(n: int):
        # Base cases for the Fibonacci sequence
        if n <= 0: 
            return 0
        if n == 1: 
            return 1
        # Checking cache for precomputed result
        if n in cache: 
            return cache[n]
        # Use recursion to compute the Fibonacci number and store in cache
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2) 
        return cache[n]
    # Returning the inner fibonacci function with access to the cache (closure)
    return fibonacci

# Call caching_fibonacci to create a Fibonacci function with caching
fib = caching_fibonacci()
