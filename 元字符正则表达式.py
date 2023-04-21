import re
#   任意匹配字符 .
pattern='.python...'
string="abcdfphp345python_py"
result1=re.search(pattern,string)
print(result1)

#   边界限制元字符,^ 匹配开始设置，$ 匹配结束设置
pattern1="^add"
pattern2="^abc"
pattern3="py$"
pattern4="ay$"
string="abcdfphp345python_py"
result1=re.search(pattern1,string)
result2=re.search(pattern2,string)
result3=re.search(pattern3,string)
result4=re.search(pattern4,string)
print(result1)
print(result2)
print(result3)
print(result4)

#   限定符，很多可百度
pattern1="py.*n"#从py到n之间除了换行符以外任意字符，而且可以任意次数
pattern2="cd{2}"#cd中的d正好出现两次
pattern3="cd{3}"#d正好出现三次
pattern4="cd{2,}"#d至少出现两次
string="abcdddfphp345python_py"
result1=re.search(pattern1,string)
result2=re.search(pattern2,string)
result3=re.search(pattern3,string)
result4=re.search(pattern4,string)
print(result1)
print(result2)
print(result3)
print(result4)

#   模式选择符，"|"
#   "python|php"python模式或者php模式任意一个匹配


#   模式单元符，"()"，将小原子组合成一个大原子
#   (cd){1,}匹配结果：cdcdcdcd
#   cd{1,}匹配结果：cdddd