class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr1 = m - 1
        ptr2 = n - 1

        for i in range(m+n-1, -1, -1):
            if ptr2 < 0: # second array empty => stop 
                break

            # check for ptr1, prevent index -1
            if ptr1 >= 0 and nums1[ptr1] > nums2[ptr2]: 
                nums1[i] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[i] = nums2[ptr2]
                ptr2 -= 1