def bubble_sort(arr):
    """
    Bubble Sort implementation
    
    Args:
        arr: List of comparable elements
        
    Returns:
        Sorted list
    """
    n = len(arr)
    
    # Create a copy to avoid modifying original array
    sorted_arr = arr.copy()
    
    # Traverse through all array elements
    for i in range(n):
        # Flag to optimize - if no swaps occur, array is sorted
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True
        
        # If no two elements were swapped, array is sorted
        if not swapped:
            break
    
    return sorted_arr


def bubble_sort_verbose(arr):
    """
    Bubble Sort with step-by-step output for learning
    """
    n = len(arr)
    sorted_arr = arr.copy()
    
    print(f"Initial array: {sorted_arr}")
    print()
    
    for i in range(n):
        print(f"Pass {i + 1}:")
        swapped = False
        
        for j in range(0, n - i - 1):
            print(f"  Comparing {sorted_arr[j]} and {sorted_arr[j + 1]}")
            
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                print(f"  Swapped! Array: {sorted_arr}")
                swapped = True
            else:
                print(f"  No swap needed")
        
        print(f"  End of pass {i + 1}: {sorted_arr}")
        print()
        
        if not swapped:
            print("Array is sorted! Early termination.")
            break
    
    return sorted_arr


# Test the algorithm
def test_bubble_sort():
    # Test case 1: Random array
    test1 = [64, 34, 25, 12, 22, 11, 90]
    print("=== Test Case 1: Random Array ===")
    result1 = bubble_sort_verbose(test1)
    print(f"Final sorted array: {result1}")
    print()
    
    # Test case 2: Already sorted
    test2 = [1, 2, 3, 4, 5]
    print("=== Test Case 2: Already Sorted ===")
    result2 = bubble_sort(test2)
    print(f"Input: {test2}")
    print(f"Output: {result2}")
    print()
    
    # Test case 3: Reverse sorted
    test3 = [5, 4, 3, 2, 1]
    print("=== Test Case 3: Reverse Sorted ===")
    result3 = bubble_sort(test3)
    print(f"Input: {test3}")
    print(f"Output: {result3}")
    print()
    
    # Test case 4: Single element
    test4 = [42]
    print("=== Test Case 4: Single Element ===")
    result4 = bubble_sort(test4)
    print(f"Input: {test4}")
    print(f"Output: {result4}")


if __name__ == "__main__":
    test_bubble_sort()
