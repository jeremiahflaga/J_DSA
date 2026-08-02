def greatest_number_linear(array: list[int]):
    steps = 0
    if not array:
        return None

    greatest_num = 0
    for i in  array:
        steps += 1
        if i > greatest_num:
            greatest_num = i

    print("Array length: ", len(array))
    print("Steps: ", steps)
    return greatest_num

greatest_number_linear([1,2,3,4,5,6,7,8,9,10])
greatest_number_linear([1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,20])

#####################
# Aug 2, 2026
# Start: 11:13 PM
# End: 11:18 PM
#####################