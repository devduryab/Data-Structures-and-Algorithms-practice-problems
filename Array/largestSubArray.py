def findLargestSubarray(A):
    max_len = 0
    start_index = 0

    for i in range(len(A)):
        visited = set()
        min_val = max_val = A[i]

        for j in range(i, len(A)):
            # If duplicate element is found, break
            if A[j] in visited:
                break

            visited.add(A[j])
            min_val = min(min_val, A[j])
            max_val = max(max_val, A[j])

            # Check if current subarray contains all consecutive integers
            if max_val - min_val == j - i:
                if max_len < j - i + 1:
                    max_len = j - i + 1
                    start_index = i

    # Return the largest subarray
    return A[start_index:start_index + max_len], (start_index, start_index + max_len - 1)


# Example usage
A = [2, 0, 2, 1, 4, 3, 1, 0]
result, indices = findLargestSubarray(A)
print("The largest subarray is", result)
print("The start and end indices are", indices)
