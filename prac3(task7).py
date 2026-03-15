
# taking valid input using while loop
while True:
    start = int(input("Enter first number: "))
    end = int(input("Enter second number: "))
    
    if start < end:
        break
    else:
        print("First number must be smaller than second number. Try again.")

print("Prime numbers between", start, "and", end, "are:")

# checking prime numbers using for loop
for num in range(start, end + 1):
    
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)