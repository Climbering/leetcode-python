# # import time
# #
# # timenow = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
# # print(timenow)
# import datetime
#
# # 范围时间
# d_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '9:30', '%Y-%m-%d%H:%M')
# d_time1 = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '9:33', '%Y-%m-%d%H:%M')
#
# # 当前时间
# n_time = datetime.datetime.now()
# print(n_time)
# print(d_time)
# print(d_time1)
# # 判断当前时间是否在范围时间内
# if n_time > d_time and n_time < d_time1:
#     print(1)
# import datetime
# t1 = '8:30'
# t2 = '11:30'  `
# t3 = '14:30'
# t4 = '17:30'
# now = datetime.datetime.now().strftime("%H:%M")
# print("当前时间:" + now)
# if t1 < now < t2 or t3 < now <t4:
#     print("工作时间")
# else:
#     print('非工作时间')
def fun(a):
    if a > 1:
        return True

if __name__ == "__main__":
    result = fun(3)
    if not result:
        print('jia')
    elif result:
        print('zhen')