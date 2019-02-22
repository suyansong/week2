# 4.随机生成一个包含1000个字母的字符串，
# 然后统计该字符串中每个字母的数量，
# 并输出结果（要求结果以字典方式存储）
# （20分：随机生成字符串5分，统计字母数量8分，
# 以字典方式存储5分，输出结果2分）

import  random
a='abcd'
b=''
#随机生成一个包含1000个字母的字符串
for i in  range(1000):
    b+=random.choice(a)
print("字符串长度",len(b))

c={}
for i in b:
    key=c.get(i)

    if(key==None):
        c[i]= 1
    else:
        c[i]+= 1
print(c)