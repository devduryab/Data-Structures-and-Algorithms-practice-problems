def findDuplicate(nums):

    visited = [False] * (len(nums) + 1)

    for i in nums:

        if visited[i]:
            return i

        visited[i] = True
    return -1


nums = [1, 2, 3, 4, 4]
print('The duplicate element is', findDuplicate(nums))
