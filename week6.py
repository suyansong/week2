
def shuru(s):
    with open("abc.txt","a") as f:
        f.write(s)
while 1:
    s = input("请输入要录入的语句:")
    if s != "exit":
        shuru(s)
    else:
        break




f=open('d://ff.txt','a')
while 1:
    print('请输入信息')
    x = input()
    if x=='exit':
        break
    else:
        f.write(x)
f.close()    这个是追加的




































