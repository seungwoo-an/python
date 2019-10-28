'''
kg1 = float(input("첫 번째 물건의 무게를 입력하시오 : "))
kg2 = float(input("두 번째 물건의 무게를 입력하시오 : "))

# print("\n현재 엘리베이터에 허용무게는 %.2fkg 입니다."%(600-kg1-kg2))
print("\n현재 엘리베이터에 허용무게는 %.2fkg 입니다."%(600-(kg1+kg2)))

'''
'''
kg1 = float(input("첫 번째 물건의 무게를 입력하시오 : "))
kg2 = float(input("두 번째 물건의 무게를 입력하시오 : "))
kg3 = 600-kg1-kg2

print("\n현재 엘리베이터에 허용무게는 %.2fkg 입니다."%kg3)
'''
'''
nowtall = int(input("키를 입력하세요 : "))
kg = (nowtall - 100)*0.9
print("표준체중은 %.1f 입니다."%kg)

print()
print("표준체중은 %.1f 입니다."%((nowtall-100)*0.9))
'''
'''
#답안
hight = float(input("키를 입력하세요 : "))
print("표준체중 : %.2fkg"%((hight-100)*0.9))
'''
'''
hight = float(input("키를 입력하세요 : "))
weight = float(input("현재 체중을 입력하세요 : "))
kg1 = (hight - 100)*0.9
kg2 = (weight/kg1)*100
print("표준 체중은 %.1f이고 비만도(%%)는 %.2f%%입니다."%(kg1,kg2)) # %% > %로 출력
'''
'''

name = input("학생 이름 : ")
korean = int(input("국어 점수 : "))
eng = int(input("영어 점수 : "))
math = int(input("수학 점수 : "))
sum_=korean + eng + math
avg = sum_/3
print("====================학생 정보====================")
print("이름\t국어\t영어\t수학\t합계\t평균")
print("%s\t%d\t%d\t%d\t%d\t%.2f"%(name,korean,eng,math,sum_,avg))
'''
'''
name = input("학생 이름 : ")
korean = float(input("국어 점수 : "))
eng = float(input("영어 점수 : "))
math = float(input("수학 점수 : "))
sum_=korean + eng + math
avg = sum_/3
print("====================학생 정보====================")
print("이름\t국어\t영어\t수학\t합계\t평균")
print("%s\t%.0f\t%.0f\t%.0f\t%.0f\t%.2f"%(name,korean,eng,math,sum_,avg))
'''
'''
산술연산자
= 대입
+ 더하기
- 빼기
* 곱하기
/ 나누기
// 나누기(몫)
% 나머지 값
** 제곱
'''
'''

num1=9; num2=2

print(num1," + ",num2," = ",num1+num2)
print(num1," - ",num2," = ",num1-num2)
print(num1," * ",num2," = ",num1*num2)
print(num1," / ",num2," = ",num1/num2)
print(num1," // ",num2," = ",num1//num2)
print(num1," % ",num2," = ",num1%num2)
print(num1," ** ",num2," = ",num1**num2)
'''
'''
관계연산자(참 : true, 거짓 : flase)
a<b a가 b보다 작다
a>b a가 b보다 크다
a<=b a가 b보다 작거나 같다
a>=b a가 b보다 크거나 같다
a==b a가 b와 같다
a!=b a가 b와 같지 않다
'''
'''
su1=3.1;su2=3

print("su1 >= su2 : %d"%(su1>=su2)) # true = 1 false = 0
print("su1 <= su2 : %d"%(su1<=su2))
print("su1 == su2 : %d"%(su1==su2))
print("su1 != su2 : %d"%(su1!=su2))

print()

su1=3.1;su2=3

print("su1 >= su2 : %f"%(su1>=su2)) # true = 1 false = 0
print("su1 <= su2 : %f"%(su1<=su2))
print("su1 == su2 : %f"%(su1==su2))
print("su1 != su2 : %f"%(su1!=su2))

print()
su1=3.1;su2=3

print("su1 >= su2 : %s"%(su1>=su2)) 
print("su1 <= su2 : %s"%(su1<=su2))
print("su1 == su2 : %s"%(su1==su2))
print("su1 != su2 : %s"%(su1!=su2))

print()
su1=3.1;su2=3

print("su1 >= su2 : %c"%(su1>=su2)) 
print("su1 <= su2 : %c"%(su1<=su2))
print("su1 == su2 : %c"%(su1==su2))
print("su1 != su2 : %c"%(su1!=su2))

'''
'''
복합 대입 연산자

a += b : a = a + b
a -= b : a = a - b
a *= b : a = a * b
a /= b : a = a / b
a //= b : a = a // b
a %= b : a = a % b
a **= b : a = a ** b
'''
'''
su1 += 1
> 6

su1 -= 1
> 5

su1 * = su2
> 25

su1 //= su2
> 5

su1 %= su2
> 0

'''
'''
su1=su2=5
su1+=1
print("su1 + 1 = ",su1)
su1-=1
print("su1 - 1 = ",su1)
su1*=su2
print("su1 * su2 = ",su1)
su1//=su2
print("su1 // su2 = ",su1)
su1%=su2
print("su1 % su2 = ",su1)
'''
'''

su1=5
su2=3
su1**=su2
su1-=2
print("su1 / 4 = ",su1/4)
print("su1 // 4 = ",su1//4)
print("su1 % 4 = ",su1%4)
'''
'''
123

30.75

30

3

'''
'''
#아주중요
논리 연산자
(a>b) and (a<c) a>b 이고 a<c 이면 참 (앞이 거짓인 경우, 뒤에 해석 안함)
(a>b) or (a<c) a>b 이거나 a<c 이면 참 (앞이 참인 경우, 뒤에 해석 안함)
not(a==b) a==b 이면 거짓
'''
'''

print(0 or 0,":",False or False)
print(1 or 0,":",True or False)
print(0 or 1,":",False or True)
print(1 or 1,":",True or True)

print("not : ",not(0 or 0),":",not(False or False)) # not 은 정수가 아닌 True / Flase 로 표현
print("not : ",not(1 or 1),":",not(True or Ture))

print(0 or 10,":",True or True) # > 숫자로 표현됨

'''
'''
#버그가 발생할수 있음
a=20
b=10
print( 0 or 0,":",False or (a+b))
print( 1 or 0,":",True or (a+b))
print( 0 and 0,":",False and (a+b))
print( 1 and 0,":",True and (a+b))
'''
'''
비트 연산자
비트연산자 / 사용 예 / 의미
| / a | b / a 와 b를 bit로 변환하여 OR 연산
    같은 숫자 | 같은 숫자 : 같은 숫자
& / a & b / a 와 b를 bit로 변환하여 AND 연산
    같은 숫자 & 같은 숫자 : 같은 숫자
^ / a ^ b / a 와 b를 bit로 변환하여 XOR 연산 (같은 자리수에 같은 숫자 > 0 , 다른 숫자 > 1)
    같은 숫자 ^ 같은 숫자 : 0
~ / ~a / a를 bit로 변환하여 NOT 연산 (양수 > 음수 , 음수 > 양수)
    * 2진수에서 양수 > 음수 하면 1이 커진다 ~10 > -11
                음수 > 양수 하면 1이 작아진다 ~-11 > 10
                
    * 2진수(8비트) 가장 왼쪽에 1 쓰면 음수
    * 보수 > 10진수 1의 보수는 9    
>> / a >> 2 / a를 bit로 변환하여 오른쪽으로 Shift 20>>2 (10100 : 101) 5
                                                20 >> 6 : 0 (2의 0승 밑으로 가면 버림 0이 됨)
<< / a << 2 / a를 bit로 변환하여 왼쪽으로 Shift 5<<2 (101 : 10100) 20
'''
'''



