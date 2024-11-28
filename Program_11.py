# Program to find even and odd number in list
even_odd_list = [10, 501, 22, 37, 100, 999, 87, 351]
even = []   # a list for even numbers
odd = []    # a list for odd numbers

for i in even_odd_list:   # for each number in the original list,
    if i % 2 == 0:        # if dividing the number by 2 gives a remainder of 0,
        even.append(i)    # add the number to the list named even using Python's list append() method
    else:
        odd.append(i)     # otherwise, append it to the list named odd

# prints out the contents of both lists
print("The Even number:",even)
print("The odd number:",odd)