# 简单的异常案例
# 给出提示信息
try:
    num = int(input("plz input your nuber:"))
    rst = 100/num
    print("计算结果是:{0}".format(rst))
    # 捕获异常后，把异常实例化，给出信息会在实例
    # 注意以下写法
    # 以下语法是捕获ZeroDivisionError异常并实例化e
    # 如果是多种error的情况
    # 需要把越具体的错误，越往前放
    # 在异常的类继承关系中，越是子类的异常，越往后放
    # 越是父类异常的时候，越往后放
    # 在处理异常的时候，一旦拦截到某一个异常，则不在继续往下查看，直接进行下一个
    # 代码，既有finally，则执行finally语句块，否则就执行下一个大的语句


except ZeroDivisionError as e:
    print("你特妈的输入的啥玩意儿")
    print(e)
    # exit时退出程序的意思
    exit()
except NameError as e:
    print("名字起错了")
    print(e)
    exit()
except AttributeError as e:
    print("好像属性有问题")
    print(e)
except Exception as e:
    # 所有异常都是继承自Exception
    # 如果写上下面这句话，任何异常都会拦截住
    # 而且，下面这句话一定是最后一个exception
    print("我也不知道就出错了")
    print(e)
    print("hahahahaha")