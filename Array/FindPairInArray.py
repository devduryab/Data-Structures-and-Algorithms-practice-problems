# Example
# Input Array
# nums = [8, 7, 2, 5, 3, 1]
# target = 10
# Output 
# pair found at (8, 2)
# paior found at (7, 3)


def findAllPairs(nums, target):
    pairs = []  # List to store all pairs

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pairs.append((nums[i], nums[j]))

    if pairs:
        for pair in pairs:
            print("pair found:", pair)
    else:
        print("pair not found")

nums = [8, 7, 2, 5, 3, 1]
target = 10

findAllPairs(nums, target)
