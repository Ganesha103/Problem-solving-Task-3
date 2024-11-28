# Find the sum of first and last digit in integer
num = int(input("Enter the Integer"))

last_digit = num % 10  # Get the last digit

first_digit = num
while first_digit >= 10: # Get the first digit by continuously dividing by 10
    first_digit //= 10

sum_digit = first_digit + last_digit  # Sum of the first and last digits

print("Sum of the first and last digits:",sum_digit)
