# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def edit_distance(str1, str2):
    m, n = len(str1), len(str2)    #取得字符串的长度
    dp = [[0 for x in range(n+1)] for x in range(m+1)]   #二维列表存储编辑距离
    if m == 0:
        return n
    elif n== 0:
        return m
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
    return dp[m][n]
if __name__ == '__main__':
    str1 = input()  #终端输入字符串
    str2 = input()  #终端输入字符串
    print(str1 + str2)
    print(edit_distance(str1, str2))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
