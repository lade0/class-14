# finding the factorial using recursion
def factorial(z):
    if z==0 or z==1:
        return 1
    else:
        return z*factorial(z-1)
    
print("the factorail of 0 is:",factorial(0))
print("the factorail of 3 is:",factorial(3))
