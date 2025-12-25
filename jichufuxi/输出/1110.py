#格式化输出
#%s  字符串
#%d  整数
#%f  浮点数
stu_id = 1
stu_name = "刘备"
stu_age = 18
stu_height = 181
stu_weight = 80.1
print(f"各位评委老师好，我的编号是%d，我的名字叫%s，\n我的年龄是%d，我的身\t高是%d，我的体重是%.2f" %(stu_id,stu_name,stu_age,stu_height,stu_weight))
print(f"各位评委老师好，我的编号是{stu_id}，我的名字叫{stu_name}，我的年龄是{stu_age}，我的身高是{stu_height}，我的体重是{stu_weight}")
