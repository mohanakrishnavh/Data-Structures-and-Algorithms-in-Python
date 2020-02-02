from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Time Complexity : O(n)
    Space Complexity: O(n)
    """
    n = len(nums)
    complement_map = {nums[0]: 0}

    for i in range(1, n):
        complement = target - nums[i]

        if complement in complement_map:
            return [complement_map[complement], i]
        else:
            complement_map[nums[i]] = i


print(two_sum([2, 7, 11, 15], 9))
