# find the cube using functions
def cube(number):
    return number*number*number

def check(number):
    if number%3==0:
        return cube(number)
    else:
        return False
    
print(check(12))
print(check(61))