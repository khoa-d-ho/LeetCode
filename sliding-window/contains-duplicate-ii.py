class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        char_set = set()

        # Handle the initial window
        for i in range(min(k + 1, len(nums))):
            if nums[i] in char_set:
                return True
            char_set.add(nums[i])

        # Slide the window
        left = 0
        for right in range(k + 1, len(nums)):
            char_set.remove(nums[left])
            if nums[right] in char_set:
                return True
            char_set.add(nums[right])
            left += 1

        return False
