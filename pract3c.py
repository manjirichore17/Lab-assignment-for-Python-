n = int(input("Enter a positive integer: "))
sum = 0
i = 0

if (n <= 0):
    print("Please enter a number greater than 0")
else:
    while (i <= n):
        sum = sum + i
        i = i + 1

    print("The sum of numbers from 1 to %d is : %d" % (n, sum))