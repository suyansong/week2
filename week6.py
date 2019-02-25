
c=open('D://aa.jpg','rb+')
b=c.read()
d=open('D://cc.jpg','wb+')
d.write(b)


import re

a=re.compile("\w+@\w+\.+com")
b=input("请输入您的邮箱:")
pl=re.search(a,b)
if pl:
    print("邮箱验证通过")
else:
    print("邮箱验证失败")


















































