# find happy number
happy_list_1 = [10, 501, 22, 307, 100, 999, 87, 351]
happy_list_count = 0 # created list for counting happy number

for i in happy_list_1:  # Iterate the list of numbers
    num = i
    last_number = []   # saving the previous sums to detect cycles

    while num!= 1 and num not  in last_number:
        last_number.append(num)
        num = sum(int(digit) ** 2 for digit in str(num)) # Sum of the squares of the digits

    if num == 1:   # If we reach 1, it is a happy number
        happy_list_count +=1

print("Number of happy numbers in the list:",happy_list_count)