import re
#   re.match(pattern,string,flag),flag可以放模式修正符等信息

string="apythonhellomypythonhispythonourpythonend"
pattern=".python."
result=re.match(pattern,string)
result2=re.match(pattern,string).span()
result3=re.match(pattern,string).group()#完成匹配的字符
print(result)
print(result2)
print(result3)

#   re.search()与match的不同在于search()只要字符串包含匹配字符就行，
#   match必须从第一个匹配字符开始，如果第一个字符不匹配，即使后面匹配也输出none
result4=re.search(pattern,string)
print(result4)
pattern2="hello"
result1=re.search(pattern2,string)
result2=re.match(pattern2,string)
print(result1)
print(result2)  #none

#   全局匹配函数：符合结果的字符全部匹配出来.
#   1）先使用re.compile()进行预编译
#   2）再使用findall()根据正则表达式从源字符串中将匹配的结果全部找出
#   两个式子可以直接写成一个，有效
pattern=re.compile(".python.")
result=pattern.findall(string)
print(result)

#   re.sub()：符合匹配全部替换，可以指示替换次数
pattern="python."
result1=re.sub(pattern,"php",string)
result2=re.sub(pattern,"php",string,2)
print(result1)
print(result2) 
