def first_repeating(arr):
    # Dictionary to store count of elements
    counts = {}
    
    # Fill counts
    for num in arr:
        counts[num] = counts.get(num, 0) + 1
    
    # Find first element with count > 1
    for num in arr:
        if counts[num] > 1:
            return num
    
    return None

# -------- Driver code --------
arr = [10, 5, 3, 4, 3, 5, 6]
result = first_repeating(arr)

if result is not None:
    print("First repeating element is:", result)
else:
    print("No repeating element found")