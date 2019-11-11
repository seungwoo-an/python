'''
def sum_func(x1,x2,x3=100):
    return x1+x2+x3
def display():
    a,b,c=10,20,30    
    print("매개 변수 2개 함수 호출 : ", sum_func(a,b))
    print("매개 변수 2개 함수 호출 : ", sum_func(a,b,c))
display()
''''''
def alba(day=30,time=8,won=8500):
    return day*time*won
def display():
    num=int(input("1.기본급\n2.일한 날짜 입력\n> "))
    if num==1:
        print("당신의 급여 : {}원 입니다.".format(alba()))
    elif num==2:
        day=int(input("일한 날짜 입력\n> "))
        print("당신의 급여 : {}원 입니다.".format(alba(day)))
display() 
''''''
def sum_func(*par:int):#튜플로 만들어줌, :int - 타입 변경 불
    result=0
    print("type : ",type(par))
    print("par : ",par)
    for num in par:
        result+=num
        print("num : %d"%num)
    return result;
print("매개변수 2개 함수 : %d"%sum_func(10,20))
print("매개변수 4개 함수 : %d"%sum_func(10,20,30,40))
''''''
def dic_func(**par):
    print("type(par):",type(par))#** : dictionary로 만들어줌
    print("par : ",par)
    for k in par.keys():
        print("{} : {} 명 입니다.".format(k,par[k]))
dic_func(똭뚝빽 = 123, 꿔익꿔익 = 8, test='테스뚜')
''''''
def change(a,b,c):
    return a+10,b+20,c+30
a,b,c=change(10,20,30)#리턴값을 a,b,c 각각에 저장
d=change(10,20,30)#더한 값을 튜플로 저장

print("a,b,c : ",a,b,c)
print("d : {}, type : {}".format(d,type(d)))
''''''
def swap(x,y):
    return y,x
a,b=10,20
print("바꾸기 전 : ",a,b)
a,b = swap(a,b)
print("바꾼 후 : ",a,b)
''''''
swap= lambda c,d:(d,c)#리스트, 튜플, dict로 가능
a,b=10,20
print("swap 결과 : ",swap(a,b))
''''''
lam = lambda a:a*10
hap = lambda a,b:a+b
noData = lambda : print("인자값 없는 람다")
print(lam(10))
print(hap(5,10))
noData()
''''''
print((lambda a,b:a+b)(5,7))# 인자값을 바로 넘길 수 있음
lam = lambda a,b,c=100:a+b+c# 디폴트 지정 가능
num1=1;num2=2
print(lam(num1,num2))
''''''
def test():
    print("1.게임 시작")
    print("2.게임 종료")
    num=int(input("선택 > "))
    if num==1:
        startGame()
    elif num==2:
        end()
end=lambda:print("게임 종료")
startGame = lambda:print("Game Start!!")
test()
'''
#MODULE
'''
import math #math.함수로 출처를 밝혀줘야함
print(math.pi)
print(math.factorial(5))
print(math.sqrt(5))
print(math.log10(2))
''''''
-import 선언은 모듈에 정의된 변수 함수 클래스들을 전부 현재 모듈로 불러옴
-불러온 이후에는 마치 우리 모듈 내부에 정의된 것처럼 자유롭게 호출함
-다른 모듈의 함수나 변수를 사용할 때는 이름 앞에 모듈명을 명시하여 소속을 밝히고 사용함(중복 방지)
''''''
from math import pi,factorial, sqrt #math.함수로 출처를 밝혀줄 필요가 없음
print(pi)
print(factorial(5))
print(sqrt(5))
#print(log10(2)) - 오류
''''''
from math import factorial, sqrt, pi
import math
print(factorial(5))
print(math.sqrt(5))#출처 밝혀도 되고 안밝혀도 됨
print(math.log10(2))
print(math.log10(3))
print(math.gcd(12,18))#최대공약수
''''''
import statistics
points = [65,75,55]
print("평균 : ",statistics.mean(points))
print("분산 : ",statistics.variance(points))
print("표준편차 : ",statistics.stdev(points))

import statistics as st
points = [65,75,55]
print("평균 : ",st.mean(points))
print("분산 : ",st.variance(points))
print("표준편차 : ",st.stdev(points))
''''''
import calculator as cal
from calculator import info
print("1인치 : %.2fcm"%cal.inch)
print("1~10까지 누적합 : ",cal.calc_sum(10))
info()
info()
info()
''''''
import random
for i in range(5):
    print(i," :%d"%int(10*(random.random())+1))#1~10까지 랜덤 숫자 생성
''''''
import random
for i in range(5):
    print(i," : ",random.randrange(1,11))#1~10까지 랜덤 숫자 생성
''''''
import random
for i in range(5):
    print(i," : ",int(random.random()*100))#0~99까지 random
''''''
import random
win_cnt, ls_cnt, sm_cnt=0,0,0
while True:
    print("가위 바위 보 게임을 시작합니다.")
    print("="*78)
    print("1.가위, 2.바위, 3.보, 4.종료")
    user = int(input("> "))
    com = int(random.randrange(1,4))
    if user==4:
        print("가위 바위 보 게임을 종료합니다.")
        print("="*78)
        print("이긴 횟수 : %d\n진 횟수 : %d\n비긴 횟수 : %d"%(win_cnt,ls_cnt,sm_cnt))
        break
    elif user==1:
        if com==1:
            print("비겼습니다.")
            sm_cnt+=1
        elif com==2:
            print("졌습니다.")
            ls_cnt+=1
        elif com==3:
            print("이겼습니다.")
            win_cnt+=1
    elif user==2:
        if com==1:
            print("이겼습니다.")
            win_cnt+=1
        elif com==2:
            print("비겼습니다.")
            sm_cnt+=1
        elif com==3:
            print("졌습니다.")
            ls_cnt+=1
    elif user==3:
        if com==1:
            print("졌습니다.")
            ls_cnt+=1
        elif com==2:
            print("이겼습니다.")
            win_cnt+=1
        elif com==3:
            print("비겼습니다.")
            sm_cnt+=1
'''
import random as rn
def Lotto():
    lotto=[]
    while True:
        num = int(rn.randrange(1,46))
        lotto.append(num)
        if lotto.count(num)>1:#0일 때 추가하는 코드로 바꿔도 됨
            lotto.pop()
        if len(lotto)==6:
            print("금주의 로또 : ",lotto)
            break
Lotto()
