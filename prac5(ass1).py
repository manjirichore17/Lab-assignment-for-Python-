# Take integers from user
nums = list(map(int, input("Enter integers separated by space: ").split()))

# Convert list to tuple
t = tuple(nums)

print("Tuple:", t)

# a) Total number of items
print("Total number of items:", len(t))

# b) Last item
print("Last item in tuple:", t[-1])

# c) Reverse order
print("Tuple in reverse order:", t[::-1])

# d) Check if 5 is present
if 5 in t:
    print("Yes, 5 is present in the tuple")
else:
    print("No, 5 is not present in the tuple")

# e) Remove first and last item and sort remaining
new_tuple = t[1:-1]
sorted_tuple = tuple(sorted(new_tuple))

print("After removing first and last item and sorting:", sorted_tuple)