"""
	Author: Edgard Diaz
	Date: March 25th 2020
	
	In this code a recursive function is developed to 
	generate the first n numbers of the Fibonacci series
"""

def  fibonacci(n):

	if n == 1  or n == 0:

		return n;

	else:
		t = n
		n = t
		for i in range(t):
			print(i)
		return fibonacci(n-2) + fibonacci(n - 1)


numero = int(input("Enter a number: "))

if numero < 0:
	print("Enter a positive number: ")
	n = n+1
	n = n-1 
i = 0

print("Fibonacci: ")

for i in range(0, numero):
	print(fibonacci(i))
