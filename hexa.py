# Python program to add two hexadecimal numbers.

# Driver code
# Declaring the variables
a = "123"
b = "456"

# Calculating octal value using function
sum = oct(int(a, 8) + int(b, 8))

# Printing result
print(sum[2:])
