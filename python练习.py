
"""
#   str.format方法1
print('{2}*{1}={0}'.format(5*3,3,5))

#   str.format方法2
print('我是{name}，今年{age}'.format(name='王伟', age=18))

#   f-strings(格式化字符串字面值)
a=5
b=3
print(f'{a}-{b}={a-b}')

#   :.mf(控制输出浮点数小数点后m位数字)
c=5
d=3
print(f'{c}/{d}={c/d:.2f}')
print('{}/{}={:.4f}'.format(a,b,a/b))


#   +(字符串拼接)
afaired='我儿'
age=18
print('余时发是'+afaired+'今年'+str(age))

#   input()
#   input(['输入年龄']),这种list里面写str是什么用？
"""

'''
age2=input('age=')
print(type(age2))
e=input('e:')
f=input('f:')
print(e+f)
print(int(a)+int(b))

name=input('你的名字叫：')
print(f'你真的叫{name}?')
'''

'''
#变量与赋值
pi=3.14
radius=4
area=pi*(radius**2)
print(area)
radius=6
area=pi*(radius**2)
print(area)

'''

'''
多变量同步赋值
    a,b,c=3,5,8(相当于元组(3,5,8))
    '='右边可以是元组、列表
    a,b,c=(3,5,8)
    a,b,c=[3,6,9]
    '='右边可以是字符串
    a,b,c='369'
    '='右边可以是range
    a,b,c=range(3,10,3)         #range（开始值，结束值，步进值）
    
    '='可以交换变量值
    a,b=5,10
    a,b=b,a
    
'''


'''
#日期输出格式化
year=input()
month=input()
date=input()
print(year, month, date)
#格式为 ：年 月 日 。中间有空格，用‘逗号’分隔
print(year, month, date, sep='/')
#以斜杠进行间隔
print(month,date,year,sep=',')
#逗号进行分割
print('{}年{}月{}日'.format(year,month,date))
#用str.format()格式输出
print(year+'年'+month+'月'+date+'日')
#用字符串拼接方式

'''


'''
四则运算
eval()函数，字符串转数值


a=float(input())
b=float(input())

for i in '+-*/':
    print('{}{}{}={:.3f}'.format(a, i,b,eval(str(a)+i+str(b))))

'''


'''
print('aa','bb') 
s=input()
print('欢迎你,',s)

print(f'欢迎你,{input()}')

print("'Hello, World!'")
a=float(input())
print('{:.3f}'.format(a))
'''


'''
name=input()
print('欢迎你,'+name)
'''


'''
year=input()
month=input()
date=input()
print(year, month, date)
#-分割
print(year, month, date, sep='-')
#以斜杠进行间隔
print(year, month, date, sep='/')
#逗号进行分割
print(month,date,year,sep=',')
#用str.format()格式输出
print('{}年{}月{}日'.format(year,month,date))
#用字符串拼接方式
print(year+'年'+month+'月'+date+'日')
'''


'''
print(5.02/0.1)
print('{:.2f}'.format(5.02/0.1))

side=input()
perimeter=side*4
print(perimeter)#如果s=2，print:'2222'

side=input()
perimeter=int(side)*4
print(perimeter)#如果s=2，print:8

side=int(input())
perimeter=side*4
print(perimeter)#如果s=2，print:8
'''


'''
print(int(3.13))
print(int('0B11111010', base=2))
print(int('11111010', base=2))
print(int('0b11111010', 2))
print(int('11111010', 2))

print(float('3.0'))
print(float(3))
print(float('   3.0\n'))
print(float('\t   3.0\n'))


radius = float(input())       
area = 3.14 * radius ** 2
print(round(area, 2))  

radius = float(input())       
area = 3.14 * radius * radius
print(round(area, 2))  

#radius = input()
#print(round(3.14 * radius ** 2, 2))
      
radius = float(input())
print(round(3.14 * radius * radius, 2))           

'''


'''
from math import pi
radius = float(input())            
area = math.pi * radius ** 2     
print(round(area, 2))      
'''



#插入法排序
#定义函数
def insertionSort(arr): 
    #从1到arr长度循环
    for i in range(1, len(arr)): 
        #key等于要插入的数
        key = arr[i]  
        j = i-1
        while j >=0 and key < arr[j] : 
                #当j大于等于0并且判断数小于arr[j]时，前面的数往后移
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
arr = [12, 11, 13, 5, 6] 
insertionSort(arr) 
print ("插入排序后的数组:{}".format(arr)) 


#选择法排序

A = [64, 25, 12, 22, 11] 
for i in range(len(A)): 
    #假设最小的数是A[i]，
    min_idx = i 
    #从i+1，到len-1遍历
    for j in range(i+1, len(A)): 
        #只要小就交换
        if A[min_idx] > A[j]: 
            min_idx = j 
    A[i], A[min_idx] = A[min_idx], A[i] 
print ("选择排序后的数组:{}".format(A)) 
    
#冒泡排序
def bubbleSort(arr):
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        # Last i elements are already in place
        for j in range(n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
arr = [64, 34, 25, 12, 22, 11, 90]
 
bubbleSort(arr)
print ("冒泡排序后的数组:{}".format(arr))  

'''

#找到第一个最大的数
def max_num(list):
    for i in range(list):
        print(list)


#定义列表
a=[3,1,2,5,7,12,47,15,29,31]

inlow=0
print(max_num(a))

'''





























      