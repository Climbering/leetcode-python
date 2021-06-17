import math
class Solution:
    def findMediansortedArray(self,num1, num2):
        #num1 = [1, 4, 6, 8,10]
        #num2 = [2,4,5,9,12,14]
        num = num1 + num2
        print(sorted(num))
if __name__ == '__main__':
    Solution().findMediansortedArray([1, 4, 6, 8,10], [2,4,5,9,12,14])
    nums = [6,43,31,44,6]
    nums1 = [3,6,9,3,5]
    nums2 = nums+nums1
    nums2.sort()
    nums.sort()
    print(nums)
    print(nums2)
