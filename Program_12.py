# count all prime number in list
prime_list_1 = [10, 501, 22, 307, 100, 999, 87, 351]
prime_list_2 = []
count = 0
for i in prime_list_1:
    c = 0
    for j in range(1,i):
        if i % j == 0:
            c +=1
    if c == 1:
        prime_list_2.append(i)
        count = count + 1

print(prime_list_2)
print(count)