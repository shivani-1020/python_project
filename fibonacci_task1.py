from os import system
system('cls')
def fibonacci_generator(n):
	a, b = 0, 1
	for _ in range(n):
		yield a
		a, b = b, a + b

# Example usage:
n = 10
result = list(fibonacci_generator(n))
print(f"Fibonacci series with {n} elements:", result)
