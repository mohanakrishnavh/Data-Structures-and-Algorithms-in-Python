from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Time Complexity : O(n)
    Space Complexity: O(n)
    """
    diff = target - nums[0]
    diff_map = {diff: 0}

    for i in range(1, len(nums)):
        diff = target - nums[i]

        if nums[i] in diff_map:
            return [nums[diff_map[nums[i]]], nums[i]]

        diff_map[diff] = i


def two_sum_2(nums: List[int], target: int) -> List[int]:
    """
    Time Complexity : O(n)
    Space Complexity: O(1)
    """
    hash_set = set()

    for item in nums:
        if (target-item) in hash_set:
            return [target-item, item]

        hash_set.add(item)


print(two_sum([1, 21, 3, 14, 5, 60, 7, 6], 81))
print(two_sum_2([1, 21, 3, 14, 5, 60, 7, 6], 81))
