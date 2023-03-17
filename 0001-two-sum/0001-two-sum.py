class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Brute-Force
        # for i in range(0,len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        #Brute-Force recursive
        # def twoSumRecur(self, nums, target, i, j):
        #     print("i: ",i,", j: ",j)
        #     if i < j < len(nums):
        #         print("sum: ", nums[i] + nums[j])
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        #         return twoSumRecur(self, nums, target, i, j + 1)
        #     elif i < len(nums)<=j:
        #         return twoSumRecur(self, nums, target, i+1, i+2)
        #     else:
        #         return 0
        # return twoSumRecur(self, nums, target, 0, 1)

        #Fisrt-Sort than Compare with two Pointers
        #Key Idea:
        #   if it is sorted, we know that if sum of most left and most right is less than
        #   target, increasing left pointer will help, and vise versa. This comparison will cost
        #   O(n)
        #   Sorting algoritm
        #   We can improve the Two-Sum algorithm by using better sorting algorithm, for example, Radix sort.
        #   However, for convinience, I will use .sort() function in python, which is O(nlogn).

        # Below is to save the previous index.
        i_map = {}
        for k in range(0, len(nums)):
            i_map[nums[k]] = k
        # nums.sort()
        sorted_nums = sorted(nums)
        l = 0
        r = len(nums) -1
        while l != r:
            two_sum = sorted_nums[l] + sorted_nums[r]
            if two_sum < target:
                l = l + 1
            elif two_sum > target:
                r = r - 1
            elif two_sum == target:
                if len(nums) == 2:
                    return [0,1]
                elif i_map[sorted_nums[l]] == i_map[sorted_nums[r]]:
                    i = 0
                    j = len(nums) - 1
                    while i != j:
                        if sorted_nums[l] == nums[i] and sorted_nums[r] == nums[j]:
                            return [i, j]
                        if sorted_nums[l] != nums[i]:
                            i = i + 1
                        if sorted_nums[r] != nums[j]:
                            j = j - 1
                return [i_map[sorted_nums[l]],i_map[sorted_nums[r]]]


        