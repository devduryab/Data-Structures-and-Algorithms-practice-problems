def find_duplicate_and_missing(arr):
    array_lenght = len(arr)

    # calculate the expected sum and expected square sum
    expected_sum = array_lenght * (array_lenght + 1 ) // 2
    expected_sum_square = array_lenght * (array_lenght + 1 ) * (2 * array_lenght + 1) // 6

    # calculate the actual sum and actual sum of squares in an array

    actual_sum = sum(arr)
    actual_sum_square = sum(x * x for  x in arr)

    # Difference between the actual and the expected sums

    diff_sum = expected_sum - actual_sum
    diff_sum_square = expected_sum_square - actual_sum_square

    sum_m_d = diff_sum_square // diff_sum

    missing = (diff_sum + sum_m_d) // 2
    duplicate = missing - diff_sum

    return missing, duplicate


arr = [4, 3, 6, 5, 2, 4]
print('The duplicate and missing elements are', find_duplicate_and_missing(arr))
 