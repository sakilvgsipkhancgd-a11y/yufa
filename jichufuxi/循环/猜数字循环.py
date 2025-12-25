"""
用函数表达循环综合练习
"""
import random
def guessnum():
    m = random.randint(1, 100)
    i = 0
    while True:
        i+=1
        try:#加入输入校验
            n = int(input(f"请输入你第{i}次猜测的数字(1~100)之间"))
        except ValueError:
            print("请输入有效数字")
            i-=1
            continue
        if n == m:
            print(f"恭喜你{i}次就猜对啦，喜提电冰箱一台")
            break#才对之后循环直接退出
        elif n > m:
            print("大了")
        else:
            print("小了")


guessnum()#函数调用





