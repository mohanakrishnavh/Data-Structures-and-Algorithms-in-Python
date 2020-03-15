def rotate_array(nums, k):
    """
    Time Complexity: O(n)
    """
    k %= len(nums)
    nums[k:], nums[:k] = nums[:-k], nums[-k:]

    return nums


print(rotate_array([1, 2, 3, 4, 5, 6, 7], 3))
