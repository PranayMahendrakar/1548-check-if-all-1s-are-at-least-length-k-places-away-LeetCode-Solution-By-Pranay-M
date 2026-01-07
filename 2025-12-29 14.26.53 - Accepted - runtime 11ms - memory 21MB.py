class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        # Track position of last 1 seen
        # Time: O(n), Space: O(1)
        last_one = -float('inf')  # Position of last 1
        for i, num in enumerate(nums):
            if num == 1:
                if i - last_one <= k:
                    return False
                last_one = i
        return True