'''for i in range(1,11,1):
    if i==10:
        print(i)
    else:
        print(i,end=", ")

num=10
for i in range(1,11,1):
    print("숫자\t%d"%num,end=": \n")
'''
'''
for i in range(1,31,1):
    if i%5==0:
        print(i)
    else:
        print(i,end="\t")
print("===================================")
for i in range(1,31,1):
    print(i,end="\t")
    if i%5==0:
        print()
'''
'''
print("===================================")
num=int(input("수 입력 : "))
sum=0
for i in range(1,num+1,1):
    sum+=i
print("총 합은",sum)
print("===================================")
num=int(input("수 입력 : "))
sum_even=0
sum_odd=0
for i in range(1,num+1,1):
    if i%2==0:
        sum_even+=i
    else:
        sum_odd+=i
print("짝수의 합은 : %d"%sum_even)
print("홀수의 합은 : %d"%sum_odd)
print("===================================")
''''''
for i in range(10):
    print(i)
for i in range(1,10):
    print(i)
''''''

start=int(input("시작 값 : "))
end=int(input("끝 값 : "))
print("7의 배수는 : ",end="")
for i in range(start,end):
    if i%7==0:
        print(i,end=" ")
print()
print("===================================")

sum=0
for i in range(1,101):
    if i%3==0 and i%5==0:
        sum+=i
print("3의 배수이자 5의 배수인 수들의 합",sum)
print("===================================")

sum=0
num1=int(input("첫번째 수 입력 : "))
num2=int(input("두번째 수 입력 : "))
if num1>=num2:
    for i in range(num2,num1+1):
        sum+=i
else:
    for i in range(num1,num2+1):
        sum+=i
print("%d와 %d사이 수의 합 : %d"%(num1,num2,sum))
print("===================================")

money=10
for i in range(2,31):
    money*=2
print("마지막 날 돈 : ",money)
print("===================================")
''''''
for i in [1,2,3,4,5,6,7,8,9,10]:
    print("i : ",i)
''''''
ls=[1,2,3,4,5,6,7,8,9,10]
for i in ls:
    print("i : ",i)
for i in ls:
    print(i,end=" ")
''''''
ls = [10,'test',123.123]
print("list : ",ls)
print()
for i in ls:
    print("i 에",i,"대입한 후 print()실행")
    print(type(i))
''''''
st="hello python"
for i in st:
    print("i: ",i)
''''''
st=" "
print(type(st))
'''
