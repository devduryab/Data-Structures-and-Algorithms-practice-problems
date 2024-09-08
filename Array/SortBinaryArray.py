def sort(arr):

    zeros = arr.count(0)
    k = 0
    while zeros:
        arr[k] = 0
        zeros = zeros - 1
        k = k + 1
    for k in range(k, len(arr)):
        arr[k] = 1


nums = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0]
sort(nums)
print("Sorted Number: ", nums)
