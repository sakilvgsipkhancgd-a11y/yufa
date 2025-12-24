"""
猜数字游戏
1.随机生成一个1~100的数字
2.机会无限次，猜中为止
3.提示菜的大了或者小了
4.猜中之后提示猜了几次
"""
import random
m = random.randint(1,100)
print(m)
n = int(input("请输入您猜测的结果"))
i = 1
while True:
    if n == m:
        break
    elif n > m:
        n = int(input(f"很遗憾您未能猜中，猜测的数字大了，请再次输入您猜测的数字，你已经猜测了{i}次"))
    else:
        n = int(input(f"很遗憾您未能猜中，猜测的数字小了，请再次输入您猜测的数字，你已经猜测了{i}次"))

    i += 1
print(f"恭喜你在猜测了{i}次之后终于猜对了，喜提电冰箱一台")