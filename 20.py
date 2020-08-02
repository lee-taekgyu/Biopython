try:
    num = int(input("INSERT :"))
    print(10/num)
except ZeroDivisionError:
    print("can't divide")
except ValueError:
    print("Check you num")
