def find_max(list1):
    my_list_max=list1[0]
    for i in list1:
        if i > my_list_max:
            my_list_max=i
    return my_list_max
print(find_max([1,2,3,4,5]))

    