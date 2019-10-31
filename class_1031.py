'''
#1.
day=0
rice=100000
sum_mice=2
eat_mice=20
while rice>=0:
    day+=1
    rice=rice-sum_mice*eat_mice
    if day%10==0:
        sum_mice*=2
print("총 쥐 : %d\n며칠? : %d\n쌀 : %d"%(sum_mice,day,rice))
'''
#2.
'''
print("요금을 투입 하세요")
money = int(input("> "))
while 1:
    print("{:=^30}".format("커피 자판기"))
    print("1. 커피<200>\t2. 코코아<250>\t3. 반환\t4. 종료")
    print("메뉴를 선택하세요")
    menu=int(input("> "))
    if menu==1:
        if money>=200:
            money-=200
            print("커피를 선택하셨습니다.\n남은 돈 :%d원"%money)
        else:
            print("요금이 부족합니다.\n현재 요금 : %d원"%money)
            print("1.요금 추가\t2.메뉴")
            sel = int(input("> "))
            if sel==1:
                print("요금을 추가하세요")
                money=money+int(input("> "))
                print("현재 잔액(%d)원"%money)
    elif menu==2:
        if money>=250:
            money-=250
            print("코코아를 선택하셨습니다.\n남은 돈  :%d원"%money)
        else:
            print("요금이 부족합니다.\n현재 요금 : %d원"%money)
            print("1.요금 추가\t2.메뉴")
            sel = int(input("> "))
            if sel==1:
                print("요금을 추가하세요")
                money=money+int(input("> "))
                print("현재 잔액(%d)원"%money)
    elif menu==3:
        print("잔액(%d)을 반환합니다."%money)
        money=0
    elif menu==4:
        print("종료합니다.")
        break
''''''
#자판
cnt=0
total=0
money=0
while 1:
    print("*"*48)
    print("요금을 투입 하세요")
    money=int(input("> "))
    total+=money
    if total>=200:
        print("{:=^43}".format("커피 자판기"))
        print("1.커피<200>\t2.코코아<250>\t3.반환\t4.종료")
        print("메뉴를 선택하세요(1~4)")
        menu=int(input("> "))
        if menu==1:
            total-=200
            print("커피를 선택하셨습니다.\n남은 돈 :%d원"%total)
        elif menu==2:
             total-=200
             print("코코아를 선택하셨습니다.\n남은 돈 :%d원"%total)
        elif menu==3:
            print("잔액 %d원을 반환합니다."%d)
            total=0
        elif menu==4:
            print("종료합니다.")
            break
        else:
            print("잘못된 입력입니다.")
    else:
        print("1.메뉴\t2.반환(1~2)")
        menu=int(input("> "))
        if menu==1:
            print("메뉴로 돌아갑니다.")
        elif menu==2:
            print("잔액 %d원을 반환합니다."%total)
            total=0
        else:
            print("잘못된 입력입니다.")
''''''
ls=[500,200,300,400];sum=0
print("ls: ",ls)
print("ls[0]: ",ls[0])
print("ls[1]: ",ls[1])
print("ls[2]: ",ls[2])
print("ls[3]: ",ls[3])
print("ls[0]: ",ls[-4])
print("ls[1]: ",ls[-3])
print("ls[2]: ",ls[-2])
print("ls[3]: ",ls[-1])
''''''
ls=[0,0,0,0];sum=0
ls[0]=int(input("첫 번째 숫자 입력 : "))
ls[1]=int(input("두 번째 숫자 입력 : "))
ls[2]=int(input("세 번째 숫자 입력 : "))
ls[3]=int(input("네 번째 숫자 입력 : "))

sum=ls[0]+ls[1]+ls[2]+ls[3]
print("ls[0] : ",ls[0])
print("ls[1] : ",ls[1])
print("ls[2] : ",ls[2])
print("ls[3] : ",ls[3])

print("list의 합 : %sum"%sum)
''''''
ls=[0,0,0,0];sum=0
print("len(ls) : ",len(ls))
for i in range(len(ls)):
    ls[i]=int(input(str(i)+"째 숫자 입력 : "))
    sum+=ls[i]

for i in range(len(ls)):
    print("ls[%d] : "%i,ls[i])
print("리스트의 합 : %d"%sum)
''''''
ls=[0,0,0,0]
sum, i=0,0
while i<len(ls):
    ls[i]=int(input(str(i)+"번째 숫자 입력 : "))
    sum+=ls[i]
    i+=1
else: i=0
while i<len(ls):
    print("ls[%d] : "%i,ls[i])
    i+=1
print("리스트의 합 : ",sum)
''''''
#list slicing
ls=[10,20,30,40]
print("ls : ",ls)
print("\nls[1:3] =>ls[1]~ls[2]:",ls[1:3])
print("ls[0:3] =>ls[0]~ls[2]:",ls[0:3])
print("ls[2:] =>ls[2]~ls[끝까지]:",ls[2:])
print("ls[:2] =>ls[0]~ls[1]:",ls[:2])
''''''
#얕은 복사, 같은 주소값
ls=[10,20,30,40]
arr=ls
print("ls : {} ls, id : {}".format(ls,id(ls)))
print("arr : {} arr, id : {}".format(arr,id(arr)))
''''''
#얕은 복사 2
ls=[10,20,30,40]
arr=ls
arr[2]=20000
print("ls : {} ls, id : {}".format(ls,id(ls)))
print("arr : {} arr, id : {}".format(arr,id(arr)))
''''''
#깊은 복사, 새로운 개체 생성
ls=[10,20,30,40]
arr=ls[:]
print("ls : {} ls, id : {}".format(ls,id(ls)))
print("arr : {} arr, id : {}".format(arr,id(arr)))
''''''
#깊은 복사 2
#module : 함수 모아두는 저장 파일, C:\Users\KGITBANK03\AppData\Local\Programs\Python\Python37\Lib
import copy
ls=[10,20,30,40]
#arr=ls[:]
arr=copy.deepcopy(ls)
arr[2]='deepcopy'
print("ls : {} ls, id : {}".format(ls,id(ls)))
print("arr : {} arr, id : {}".format(arr,id(arr)))
'''
ls=[10,20,30]
arr=[40,50,60]
print("ls : ",ls)
print("arr : ",arr)

Str=ls+arr
print("ls + arr => str : ",Str)
string =ls*3
print("ls*3 => string : ",string)
