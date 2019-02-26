# c=open('D://aa.jpg','rb+')
# b=c.read()
# d=open('D://cc.jpg','wb+')
# d.write(b)
#
#
# import re
#
# a=re.compile("\w+@\w+\.+com")
# b=input("请输入您的邮箱:")
# pl=re.search(a,b)
# if pl:
#     print("邮箱验证通过")
# else:
#     print("邮箱验证失败")



# numbers=[1,5,-12,37,6,93,100]
#
# even=[]
# odd=[]
# for i in range(len(numbers)):
#     if numbers[i]%2==0:
#         odd.append(numbers[i])
#     else:
#         even.append(numbers[i])
#
# print(even)
# print(odd)
#
#
#
# def shuru(s):
#     with open("abc.txt","a") as f:
#         f.write(s)
# while 1:
#     s = input("请输入要录入的语句:")
#     if s != "exit":
#         shuru(s)
#     else:
#         break
# 1. 使用while循环，实现持续的用户录入信息，
# 将录入的信息以追加的方式保存至文件中，
# 当用户输入exit时，退出程序。（50分）

# f=open('d://ff.txt','a')
# while 1:
#     print('请输入信息')
#     x = input()
#     if x=='exit':
#         break
#     else:
#         f.write(x)
# f.close()    这个是追加的



