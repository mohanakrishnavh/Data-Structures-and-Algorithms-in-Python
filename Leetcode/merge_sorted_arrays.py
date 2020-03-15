def merge_sorted_array(list_1, list_2):
    l1 = 0
    l2 = 0

    l1_length = len(list_1)
    l2_length = len(list_2)

    while l1 < l1_length and l2 < l2_length:
        if list_1[l1] < list_2[l2]:
            l1 += 1
        else:
            list_1.insert(l1, list_2[l2])
            l1 += 1
            l2 += 1

    if l2 < l2_length:
        list_1.extend(list_2[l2:])

    return list_1


array_1 = [1, 3, 4, 5]
array_2 = [2, 6, 7, 8]
print(merge_sorted_array(array_1, array_2))



