n = int(input("INSERT :"))

def Factorial(n: int):
    num = 1

    while n > 0:
        num *=n
        n -=1
    
    return num

a = Factorial(n)
print(a)
