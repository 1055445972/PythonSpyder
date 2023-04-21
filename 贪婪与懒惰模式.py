import re
pattern1='p.*y'#贪婪模式
pattern2='p.*?y'#懒惰模式
string="abcdfphp345Python_pypsfhy"
result1=re.search(pattern1,string)
result2=re.search(pattern2,string)
print(result1)
print(result2)
#贪婪模式是第一次出现和最后一次结束
#懒惰模式是第一次出现和第一次结束