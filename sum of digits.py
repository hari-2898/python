# Python program to find the sum of digits of a number
def sum_of_digits(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n //= 10
    return total
s = int(input("Enter the number: "))
result = sum_of_digits(s)
print("Sum of digits:", result)
