def find_min(list1):
    my_list_min=list1[0]
    for i in list1:
        if i < my_list_min:
            my_list_min=i
    return my_list_min
print(find_min([1,2,3,4,-5]))
