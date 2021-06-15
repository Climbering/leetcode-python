class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = ''
        length = 0
        for i in s:
            if i not in temp:
                temp+=i
                length = max(length,len(temp))
            else:
                temp+=i
                temp = temp[temp.index(i)+1:]
        return length
if __name__ == '__main__':
    solution = Solution()
    length = solution.lengthOfLongestSubstring('pwwkew')
    print(length)

