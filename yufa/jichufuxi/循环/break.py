"""
break用于直接结束循环，在达成某个条件时，直接结束循环
"""
#如下例，每天给女神送饭，每天都会表
# 白，如果女神同意或者想再看看，继续送饭，如果明确表示拒绝，则停止送饭
#此处循环实际上使用while循环更好，因为不知道循环次数

"""for i in range(10):
    if int(input("拒绝输入1，继续输入0")) == 1:
        break
print("你我无缘呐")"""
#while循环
"""p = int(input("请选择：想要继续输入0，拒绝输入1"))
while True:
    if p == 1:
        break
    p = int(input("请选择"))
print("不好意思")"""
#再来一个猜数字游戏
i  = 20
m = 1
o = False
user = int(input("请输入你要猜测的数字，这个数字在10~30之间"))
while m < 3:
    if user == 20:
        o = True
        break

    print()
    if m == 3:
        break
    m += 1
    user = int(input(f"请重新输入，请注意你还有{4 - m}次机会"))

if o :
    print(f"恭喜你{m}次就猜中了")
else:
    print("很遗憾，您未能猜中")