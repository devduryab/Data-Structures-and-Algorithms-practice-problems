# move all zeros present in an array

# Input:  { 6, 0, 8, 2, 3, 0, 4, 0, 1 }
# Output: { 6, 8, 2, 3, 4, 1, 0, 0, 0 }

def reorder(A):

    k = 0

    for i in A:
        if i:
            A[k] = i
            k = k + 1

    for i in range(k, len(A)):
        A[i] = 0


Arr = [6, 0, 8, 2, 3, 0, 4, 0, 1]
reorder(Arr)
print(Arr)
