def hasZeroSumSubarray(nums):
    seen_sums = set()
    current_sum = 0
    for num in nums:
        current_sum += num
        if current_sum == 0 or current_sum in seen_sums:
            return True
        seen_sums.add(current_sum)
    return False

nums = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
if hasZeroSumSubarray(nums):
    print("Subarray with zero-sum exists")
else:
    print("No subarray with zero-sum exists")
