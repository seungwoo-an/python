'''
num1=7
num2=5

num3=num1+num2
num4=num1-num2
num5=num1*num2
num6=num1/num2

num8=num2-num1
num9=num2/num1

print("num1+num2=%d"%num3)
print("num1-num2=%d"%num4)
print("num1*num2=%d"%num5)
print("num1/num2=%.1f"%num6)
print("num2-num1=%d"%num8)
print("num2/num1=%.1f"%num9)
'''
'''
#답안
num1=7
num2=5
sum_= num1+num2
sub = num1-num2
mul = num1*num2
div = num1/num2
print("num1+num2=%d"%sum_)
print("num1-num2=%d"%sub)
print("num1*num2=%d"%mul)
print("num1/num2=%f"%div) # 나눗셈은 가급적이면 %f 사용
'''
'''
num=100
print("파이썬 %d점"%num)

age=27
print("\n나는 %d살 이다"%age)

P=90
C=80
J=70
sum_=P+C+J
div=(P+C+J)/3
print("\n파이썬의 점수 : %d"%P)
print("C언어의 점수 : %d"%C)
print("Java의 점수 : %d"%J)
print("\n3과목의 합계 : %d"%sum_)
print("3과목의 평균 : %.2f"%div)
'''
'''
#답안
py=100
print("파이썬 %d점"%py)

age=27
print("나는",age,"살이다")

파이썬=99
씨언어=76
자바=95
총점=파이썬+씨언어+자바
평균=총점/3

print("총점 : %d"%총점)
print("평균 : %.2f"%평균)
'''
'''
sta = 11
min_=37
div=min_/sta

print("한 역을 지나는데 걸리는 시간 : %.2f분"%div)
'''
'''
#답안
st=11
time=37
avg=time/st

print("한정거장당 소요 시간 : %.2f분"%avg)
'''
'''

flt = 126.567

print("round(flt) : ",round(flt)) # round 함수는 정수까지 반올림 할 수 있다
print(flt)
print("round(flt,1) : ",round(flt,1)) # round 함수는 값을 바꿀수 있다
print("round(flt,2) : ",round(flt,2))

print("round(flt,-1) : ",round(flt,-1))

flt=round(flt,2)
print(flt)
'''
'''
sec=11.27
hour=sec/60/60

meter = 100
km=meter/1000

speed = km/hour


print("전동 자전거로 1시간 후 갈 수 있는 거리: ",round(speed,2),"km")
'''
'''
num1=0.1/11.27
print("전동 자전거로 1시간 후 갈 수 있는 거리:",round(num1*60*60,2),"km")
'''
'''
#답안
sec = 60*60
result = sec/11.27
meter=result*100
kil=meter/1000
print("1시간동안 이동 거리 : %.2fkm"%kil)
'''
'''
flt=123.123
print("%.3f + %.3f = %.3f"%(flt,321.321,flt+321.321))
print(flt,"+",321.321,"=",flt+321.321)

ch1,ch2,ch3="파",'2',"썬"
print("%c + %c + %c = %s"%(ch1,ch2,ch3,ch1+ch2+ch3))
print(ch1,"+",ch2,"+",ch3,"=",ch1+ch2+ch3)

str_1="python";str_2="test"
str_3=str_1+str_2
print("%s + %s = %s"%(str_1,str_2,str_1+str_2))
print(str_1,"+",str_2,"=",str_1+str_2)

#서로 다른 형식 이면 연산 안됨
#정수 or 실수 +(연산자) 정수 or 실수 > 덧셈
#문자열or리스트or튜플 +(연산자) 문자열or리스트or튜플 > update A+B > AB
'''
'''
변수의 자료형 확인
<class 'int'> 정수형(4바이트)
<class 'float'> 실수형(4바이트, 더블은 8바이트)
<class 'str'> 문자열(1바이트)
<class 'bool'> 블형 (true/flase 논리)

#아래는 하나에 여러 개를 넣어서 표현할 수 있음
<class 'list'>
<class 'tuple'>
<class 'set'>
<class 'tuple'>
<class 'dict'>
'''
'''

A=10
B=5

print("type :",type(A<B));print("type :",(A<B)) # 자료형을 확인하는 함수 : type
num = 100;print("type : %s"%type(num))
flt = 321.321;print("type : %s"%type(flt))
ch = "A";print("type : %s"%type(ch)) # 단일 문자라는 자료형은 없음
st = "test";print("type : %s"%type(st)) 

num = 100.0;print("type : %s"%type(num))
'''
'''
num=100
print("type : %s\tid : %s"%(type(num),id(num)))
num=321.321
print("type : %s\tid : %s"%(type(num),id(num)))
num="A"
print("type : %s\tid : %s"%(type(num),id(num)))
num="test"
print("type : %s\tid : %s"%(type(num),id(num)))
'''
'''
st1 = "Python"
st2 = "Test"
su = 100
flt = 1.11

num = '100'

print(flt+su)
print(st1 + st2)
#print(su+num)
'''
'''
su=100
print('type(su) : ',type(su)) 
print('type(str(su)) : ',type(str(su))) # 강제 형 변환 / 일회성
print('type(float(su)) : ',type(float(su)))

print('type(su) : ',type(su))

su = '100.1'
print(float(su))
#print(int(su))

su= '백점일'
#print(float(su))
'''

'''
#그냥 해본거
su="A"
print('type(su) : ',type(su))
print('type(str(su)) : ',type(str(su)))
print('type(float(su)) : ',type(float(su)))

su="산"
print('type(su) : ',type(su))
print('type(str(su)) : ',type(str(su)))
print('type(float(su)) : ',type(float(su)))
'''
'''
su = 100
num = '100'
flt = "1.111"

print(su+int(num))
print(su+float(flt))
print(str(su)+num)
'''
'''
#입력함수 : 사용자가 직접 값을 입력할수 있도로 하는 함수

'''
'''
print("숫자 입력") # 입력할 데이터에 대한 안내

num1 = input()

print("입력 받은 값 : ",num1)

'''
'''
print("이름 입력 :")
name = input()
print("나이 입력 :")
age = input()
print("%s 님의 나이는 %s살 입니다"%(name,age))
'''
'''
#오류남 
print("이름 입력 :")
name = input()
print("나이 입력 :")
age = input() #아마 문자열로 받는듯
print("%s 님의 나이는 %d살 입니다"%(name,age))
# 이렇게 하면 됨
print("이름 입력 :")
name = input()
print("나이 입력 :")
age = input()
print("%s 님의 나이는 %d살 입니다"%(name,int(age)))

'''
'''
#답안
print("이름 입력 :")
name = input()
print("나이 입력 :")
age = input()
print(name,"님의 나이는 ",age,"살 입니다")
'''
'''
print("두 수의 합을 구해 줍니다")
print("두 수 입력")

num1 = input()
num2 = input()
num3 = num1 + num2
print("두 수의 합 ",num1,"+",num2,'=',num3)
'''
'''
print("두 수의 합을 구해 줍니다")
print("두 수 입력")

num1 = input()
num2 = input()
num3 = int(num1) + int(num2)
print("두 수의 합 ",num1,"+",num2,'=',num3)
'''
'''
#그냥 해봄
num1 = int(input())
num2 = int(input())
num3 = num1 + num2
print("두 수의 합 ",num1,"+",num2,'=',num3)
'''
'''
num1=int(input())
num2=int(input())

result=num1+num2
print(num1,"+",num2,"=",result)

result=num1-num2
print(num1,"-",num2,"=",result)

result=num1*num2
print(num1,"*",num2,"=",result)

result=num1/num2
print(num1,"/",num2,"=",result)

'''
'''

print("문자열 입력")
name = input()
print("정수 입력")
age = int(input())
print("실수 입력")
flt = float(input())

print("name 값: ",name,"\t type : ",type(name))
print("age 값: ",age,"\t type : ",type(age))
print("flt 값: ",flt,"\t type : ",type(flt))

'''
'''
name = input("이름을 입력하세요 : ") # print 함수를 쓰지 않아도 됨(print 함수는 커서가 아래로 감)

age = int(input("나이를 입력하세요 : "))

addr = input("주소를 입력하세요 : ")

print("이름 : ",name,"\n나이 : ",age,"\n주소 : ",addr)
'''
'''
name = input("이름을 %d번 입력하세요 : "%10)
print(name)

name = input(10)
print(name)

name = input("이름을" "입력하세요")
print(name)

#name = input("이름을",10,"입력하세요") > 콤마가 들어가면 안됨
#print(name)
'''
'''
#그냥 해본거
year1 = int(input("올해의 년도를 %d자리로 입력하세요 : "%4))
year2 = int(input("당신이 태어난 년도를 %d자리로 입력하세요 : "%4))
age = year1-year2+1
print("\n당신의 나이는 %d살 입니다"%age)
'''

year1 = int(input("올해의 년도를 4자리로 입력하세요 : ")) #nowyear로 변경
year2 = int(input("당신이 태어난 년도를 4자리로 입력하세요 : ")) #birthyear로 변경
age = year1-year2+1
print("\n당신의 나이는 %d살 입니다"%age)
#답안
print("당신의 나이는 %d살 입니다"%(year1-year2+1))
