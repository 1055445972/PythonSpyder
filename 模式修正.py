import re
#   I：忽略大小写
#   M：多行匹配
#   ...,百度
pattern1='python'
pattern2='python'
string="abcdfphp345Python_py"
result1=re.search(pattern1,string)
result2=re.search(pattern2,string,re.I)
print(result1)
print(result2)