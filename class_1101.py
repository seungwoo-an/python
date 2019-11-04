'''
a=[1,8,5,7,5,2,6,8,8]
a.sort()#순서
a.sort(reverse=true)
a.reverse()#역
print(a)
a.insert(2,10)#2번 인덱스에 10 추가
a.remove(5)#5번 인덱스 값 삭제
print(a.index(2))#2의 값을 가지는 인덱스 반환
''''''
ls = [10,20,30]
arr = [40,50,60]
Str = [0,0,0]
string = [0,0,0]
for i in range(3):
    Str[i]=ls[i]+arr[i]
    string[i]=ls[i]*3
print("Str : ",Str)
print("string : ",string)
''''''
ls=[4,8,2,7,6]
for i in range(len(ls)-1):
   for j in range(i+1,len(ls)):#기준을 옮긴 만큼 비교 대상의 위치도 옮겨주어야 함
       if ls[i]>ls[j]:
           ls[i],ls[j]=ls[j],ls[i]
print(ls)
''''''
score=[82,85,76,79,96]
place=[1 for i in range(5)]
for i in range(len(score)):
   for j in range(len(score)):
       if score[i]<score[j]:
           place[i]+=1
print("점수 : ",score)
print("순위 : ",place)
#for i in range(5):
    print("점수 : %d\t등수 : %d"%(score[i],place[i]))
''''''
ls=[10,20,30]
ls.append(1000)
for i in range(len(ls)):
    print("ls[{}] : {}".format(i,ls[i]))
print("리스트의 총 갯수 : ",len(ls))
print("ls : ",ls)
ls=[]
print("ls초기화 후 : ",ls)
''''''
ls = []
for i in range(4):
    ls.append(0)
sum=0

for i in range(len(ls)):
    ls[i]=int(input(str(i+1)+"번째 숫자 : "))
    sum+=ls[i]

for i in range(len(ls)):
    print("입력 받은 값 ls[{}] : {}".format(i,ls[i]))
print("합계 : %d"%sum)
''''''
num=int(input("몇 개의 공간을 만드시겠습니까? : "))
ls=[]
Sum=0
for i in range(num):
    ls.append(int(input(str(i+1)+"번째 숫자 : ")))
    Sum+=ls[i]

for i in range(len(ls)):
    print("입력 받은 값 ls[{}] : {}".format(i,ls[i]))
print("합계 : ",Sum)
''''''
ls=[30,20,10]
print("현재 리스트 : ",ls)

print("pop()으로 추출한 값 : ",ls.pop())
print("pop()후 리스트 : ",ls)

ls.sort()
print("sort()후 리스트 : ",ls)

ls.reverse()
#ls.sort(reverse=true)
print("reverse()후 리스트 : ",ls)

del(ls[2])#ls.remove(10)
print("del()후 리스트 : ",ls)
''''''
ls=[30,20,10]
print("현재 리스트 : ",ls)

print("10 값의 위치 : ",ls.index(10))#제일 처음 찾은 값만 반환

ls.insert(2,200)
print("insert(2,200) 후 리스트 : ",ls)

ls.remove(200)
print("remove(200) 후 리스트 : ",ls)#제일 처음 찾은 값만 삭제

ls.extend([555,666,555])
print("ls.extend([555,666,555]) 후의 리스트 : ",ls)

print("555값의 개수 : ",ls.count(555))
''''''
#1
ls = [10,5,20,7,9,31,12,11,19,32]
print("1. ls : ",ls)
ls_even=[]
ls_odd=[]
ls_sub=[]
for i in range(len(ls)):
    if i%2==0:
        ls_even.append(ls[i])
    else:
        ls_odd.append(ls[i])

for i in range(len(ls_even)):
    ls_sub.append(ls_even[i]-ls_odd[i])
print("2. 뺀 결과 : ",ls_sub)
#2
even_sum=0
odd_sum=0
result1,result2=0,0
for i in range(len(ls)):
    if i%2==0:
        even_sum+=ls[i]
    else:
        odd_sum+=ls[i]
result_plus = even_sum+odd_sum
result_sub = even_sum-odd_sum
print("3. 합한 결과 : ",result_plus)
print("4. 뺀 결과 : ",result_sub)
#3
invertLS=[]
for i in range(len(ls)):
    invertLS.append(ls.pop())
print("5-1. invertLS : ",invertLS)
ls = [10,5,20,7,9,31,12,11,19,32]
invertLS=[]
for i in range(1,11):
    i*=-1
    invertLS.append(ls[i])
print("5-2. invertLS : ",invertLS)
#4.
ls = [10,5,20,7,9,31,12,11,19,32]#위에서 pop()으로 다 날렸기 때문에 새로 선언
sortLS = ls[:]#깊은 복사
for i in range(len(ls)-1):
   for j in range(i+1,len(ls)):
       if sortLS[i]>sortLS[j]:
           sortLS[i],sortLS[j]=sortLS[j],sortLS[i]
print("6. sortLS : ",sortLS)
#5.
reverseLS = ls[:]
for i in range(len(ls)-1):
   for j in range(i+1,len(ls)):
       if reverseLS[i]<reverseLS[j]:
           reverseLS[i],reverseLS[j]=reverseLS[j],reverseLS[i]
print("7. reverseLS : ",reverseLS)
'''
