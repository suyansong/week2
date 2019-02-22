# 2. 编写程序，生成一个包含50个随机整数的列表，
# 随机整数的范围是从-10到10，然后将列表中所有的正数存为一个新的子列表，
# 负数存为另一个新的子列表。（15分：生成随机列表5分
# ，得出正负数新列表各5分）

import random

a=[]
c=[]
for i in range(50):
    b=random.randint(-10,10)
    if b>0:
        a.append(b)
    else:
        c.append(b)
print(a)
print(c)
