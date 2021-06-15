class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dic = {}

        for i in range(len(nums)):
            tmp = target - nums[i]

            if tmp in dic:
                return dic[tmp], i
            else:
                dic[nums[i]] = i

        return None
if __name__ == '__main__':
    nums = [2, 3, 4,6,8]
    solution = Solution()
    print(solution.twoSum(nums, 10))
