num = [4, 5, 2, 2, 5, 7, 8, 4, 3] # Given list of integers

found_non_repeating = False # find the first non-repeating element

for i in range(len(num)):
    is_repeating = False
    for j in range(len(num)):  # Compare the current element with the rest of the elements in the list
        if i != j and num[i] == num[j]:
            is_repeating = True
            break  # If found repeating, no need to check further
    if is_repeating == False:  # If the current element is not repeating, it's the first non-repeating element
        print(f"The first non-repeating element is: {num[i]}")
        found_non_repeating = True
        break  # We found the first non-repeating element, no need to continue

# If no non-repeating element was found, print a message
if found_non_repeating == False:
    print("There are no non-repeating elements in the list.")