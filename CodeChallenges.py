#WAP to find the factorial of a number:

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

n=int(input("Enter a positive integer: "))
fact=factorial(n)

print("The factorial of", n, "is", fact)
