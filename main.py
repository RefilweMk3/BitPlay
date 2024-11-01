def numberOfBits(n):
    ones = 0
    zeros = 0
    while(n):
        if (n & 1 == 1):
            ones += 1
        else:
            zeros += 1
        n>>= 1
        print("Number of ones =", ones, "\nNumber of zeros =", zeros)

number = int(input("Enter you number: "))
numberOfBits(number)