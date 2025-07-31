class Solution:
    def twoSum(self, nums, target):
        """
        Hash Map approach - O(n) time complexity
        
        Args:
            nums: List of integers
            target: Target sum
            
        Returns:
            List of two indices that sum to target
        """
        # Hash map to store number and its index
        num_to_index = {}
        
        for i, num in enumerate(nums):
            # Calculate what number we need to reach the target
            complement = target - num
            
            # If complement exists in hash map, we found our answer
            if complement in num_to_index:
                return [num_to_index[complement], i]
            
            # Store current number and its index
            num_to_index[num] = i
        
        # Should never reach here given problem constraints
        return []

    def twoSum_bruteforce(self, nums, target):
        """
        Brute force approach - O(n²) time complexity
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


# Test cases
def test_two_sum():
    solution = Solution()
    
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = solution.twoSum(nums1, target1)
    print(f"Input: {nums1}, Target: {target1}")
    print(f"Output: {result1}")
    print(f"Expected: [0, 1]")
    print()
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = solution.twoSum(nums2, target2)
    print(f"Input: {nums2}, Target: {target2}")
    print(f"Output: {result2}")
    print(f"Expected: [1, 2]")
    print()
    
    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    result3 = solution.twoSum(nums3, target3)
    print(f"Input: {nums3}, Target: {target3}")
    print(f"Output: {result3}")
    print(f"Expected: [0, 1]")

if __name__ == "__main__":
    test_two_sum()
