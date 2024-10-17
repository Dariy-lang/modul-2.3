my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
count = 0
while count < len(my_list):
    x = my_list[count]
    count = count + 1
    if x == 0:
        continue
    elif x < 0:
        print(x)
        break
    elif count == len(my_list):
        print(x)
    else:
        print(x)








