def setOrNot(number,n):
    mask = 1
    if (n & mask) == 1 or (n & mask) == 0:
        if number & (1 << (n-1)):
            print("Set")
        else:
            print("Not Set")
number = int(input("Enter the number: "))
n = int(input("Enter the bit position: "))
setOrNot(number, n)