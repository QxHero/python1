# 简单的异常案例
try:
    num = int(input("plz input your nuber:"))
    rst = 100/num
    print("计算结果是:{0}".format(rst))
except:
    print("你特妈的输入的啥玩意儿")
    # exit时退出程序的意思
    exit()