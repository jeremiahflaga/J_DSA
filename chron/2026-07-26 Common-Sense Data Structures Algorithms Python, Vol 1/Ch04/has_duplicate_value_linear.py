def has_duplicate_value_linear(array: list[int]):
    # create an array with eleven zeros; for keeping track of  11 possible ratings (0 to 10)
    existing_numbers = [0] * 11

    for i in range(len(array)):
        if existing_numbers[array[i]] == 1:
            return True
        else:
            existing_numbers[array[i]] = 1

    return False