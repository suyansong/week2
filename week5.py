# 5.实现以下功能：（30分）
# 	s='The column above illustrates apparently' \
#   ' the polularity of people ' \
#   'doing exercise in a certain year ' \
#   'from 2013 to 2018.Based upon the data,' \
#   'we can see that python is wonderful. ' \
#   'python is wonderful. Python ' \
# 对这段文字中的单词进行数字统计，并且进行个数升序
# （能够生成字典8分，字典中统计数正确7分，进行排序8分，最后实现结果7分）
s='The column above illustrates apparently' \
  ' the polularity of people ' \
  'doing exercise in a certain year ' \
  'from 2013 to 2018.Based upon the data,' \
  'we can see that python is wonderful. ' \
  'python is wonderful. Python '


print("原字符串:",s)
s=s.replace(".","")
print("替换后的字符串:",s)

s=s.split(" ")
print("原列表",s)
# 去除切割后最后一个空字符
s.pop()
print("去除空字符列表",s)
dict={}
for i in s:
    key = dict.get(i)
    # 每个单词的数量，
    if(key==None):
        dict[i]=1
    else:
        dict[i]+=1

dict1={}
#  单词个数排序
sv=list(dict.values())
sv.sort()

# 去除个数相同，减少循环次数
sv=set(sv)
sv=list(sv)
# 实现单词排序
for i in sv:
    for j in dict:
        if(dict[j]==i):
            dict1[j]=i

# 输出结果
print(dict1)
