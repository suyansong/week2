# 1.用python语句判断所输入的手机号，是否正确
# 要对手机号的号段进行判断，号段任意给出6个作为模拟号段即可.
# 判断手机号码是否是由数字组成的(总分15分
# ，5分能够判断是否为数字，5分判断是否为有效号段
# ，5分实现)
#

tel=input("请输入手机号:")
pop=[137,135,176,177,145,189]
try:
    # 判断是不是纯数字
    int(tel)
    if(len(tel)==11):
        a=tel[0:3]
        bool=False
        for i in pop:
            if(int(a)==(i)):
                bool=True
                break
        if(bool):
            print("有效的手机号")
        else:
            print("无效的手机号")
    else:
        print("输入的不是有效的手机号！")
except ValueError:
    print("输入的不是有效的手机号")