import re
#   普通字符作为原子
patten="yue"
string="http://yum.iqianyue.com"
result1=re.search(patten,string)
print(result1)

#   非打印字符作为原子，什么是非打印字符：格式控制符
#   string因为有换行所以有输出，如果全部写在一行则返回none
patten="\n"
string='''http://yum.iqianyue.com
http://baidu.com'''
result1=re.search(patten,string)
print(result1)

#   通用字符作为原子，什么是通用字符：一个原子匹配一类字符
#   \w:任意一个字母、数字、下划线
#   \d:任意一个十进制数
#   百度有很多
pattern='\w\dpython\w'
string="abcdfphp345python_py"
result1=re.search(pattern,string)
print(result1)

#   原子表：由[]表示
#   [xyz]py,可以匹配'xpy','ypy','zpy'
#   [^xyz]py,除了xyz都可以匹配
pattern1="\w\dpython[xyz]\w"
pattern2="\w\dpython[^xyz]\w"
pattern3="\w\dpython[xyz]\W"
string="abcdfphp345python_py"
result1=re.search(pattern1,string)
result2=re.search(pattern2,string)
result3=re.search(pattern3,string)
print(result1)
print(result2)
print(result3)