"""
Original problem
https://leetcode.com/problems/median-of-two-sorted-arrays/
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
from typing import List

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float :
        new_list = []

        len_1, len_2 = len(nums1), len(nums2)
        idx_1, idx_2 = 0, 0
    
        while(len(new_list) < len_1 + len_2) :
            if idx_1 == len_1 :
                new_list.append(nums2[idx_2])
                idx_2 += 1
            elif idx_2 == len_2 :
                new_list.append(nums1[idx_1])
                idx_1 += 1
            else :
                if nums1[idx_1] <= nums2[idx_2] :
                    new_list.append(nums1[idx_1])
                    idx_1 += 1
                else :
                    new_list.append(nums2[idx_2])
                    idx_2 += 1

        return self.find_median(new_list)

    def find_median(self, nums : List[int]) :
        if len(nums) == 0 :
            return None
        elif len(nums) == 1 :
            return nums[0]
        else :
            len_nums = len(nums)
            idx_half = int(len_nums / 2)
            if len_nums % 2 == 0 :
                # Even number of elements
                return (nums[idx_half - 1] + nums[idx_half]) / 2
            else :
                # Odd number of elements
                return nums[idx_half]

        

class Solution_WRONG:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float :
        median_1 = self.find_median_array(nums1)
        median_2 = self.find_median_array(nums2)
        
        if median_1 is None : return median_2
        if median_2 is None : return median_1

        return (median_1 + median_2) / 2

    def find_median_array(self, nums : List[int]) :
        if len(nums) == 0 :
            return None
        elif len(nums) == 1 :
            return nums[0]
        else :
            len_nums = len(nums)
            idx_half = int(len_nums / 2)
            if len_nums % 2 == 0 :
                # Even number of elements
                return (nums[idx_half - 1] + nums[idx_half]) / 2
            else :
                # Odd number of elements
                return nums[idx_half]

        
