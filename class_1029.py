'''
num_a, num_s, num_=0,0,0
for i in st:
    num_+=1
    if i=='a':
        num_a+=1
    elif i=='s':
        num_s+=1

print('※결과')
print("※총 개수 : ",num_)
print("※a 개수 : ",num_a)
print("※s 개수 : ",num_s)
#print("총 개수 : %d\na 개수 : %d\ns 개수 : %d"%(num_,num_a,num_s))
''''''
print("{0}+{1}={2}".format(10,2,10+2))
print("{2}+{1}={0}".format(10,2,10+2))
print("{}+{}={}".format(10,2,10+2))

print("{:,}".format(1000000))

print("{:<10},왼쪽정렬,{:0<10}".format('첫번째','두번째'))
print("{:>10},오른쪽정렬,{:9>10}".format('첫번째','두번째'))
print("{:*^10},가운데정렬,{:5^10}".format('첫번째','두번째'))
''''''
for i in range(0,3,1):
    for k in range(0,5,1):
        print("이중 for문 (i:%d\tk:%d)"%(i,k))

for i in range(0,3,1):
    for k in range(0,5,1):
        print("(i:%d\tk:%d)"%(i,k),end=" ")
    print("")

'''
'''
print("{:-^60}".format(" 구 구 단 "))
for i in range(2,10):
    print(" %d단"%i,end="\t")
    #print("{:^5}".format('%d단'%i),end="\t")
print("")
print("-"*63)
for i in range(1,10):
    for k in range(2,10):
        print("%d*%d=%d"%(k,i,i*k),end="\t")
    print()
print("-"*63)
''''''
for i in range(5):
    print("상위포문 %d일 때 하위 포문 :"%i,end="")
    if i==0:
        for k in range(5):
            print(i,end=" ")
        print()
    else:
        for k in range(0,i*4+1,i):
            print(k,end=" ")
        print()
#이중 for문에서 for j in range(5):
                    print(i*j,end=" ")
                print()
''''''
sec=11.27
hour=sec/60/60

meter = 100
km=meter/1000

speed = km/hour


print("전동 자전거로 1시간 후 갈 수 있는 거리: ",round(speed,2),"km")
''''''
name = input("이름을 %d번 입력하세요 : "%10)

name = input(10)
'''
#1
for i in range(1,22,5):
    for j in range(i,i+5):
        print(j,end="\t")
    print()
print('='*60)
#2
for i in range(1,22,5):
    for j in range(5):
        print(i+j,end="\t")
    print()
print('='*60)
#3
for i in range(5):
    for j in range(5):
        print(1+5*i+j,end="\t")
    print()
print('='*60)
#4
for i in range(1,22,5):
    print(i,end='\t')
    for j in range(1,5):
        print(i+j,end="\t")
    print()
print('='*60)
#5
for i in range(0,5):
    for j in range(1,6):
        print(j+5*i,end='\t')
    print()
print('='*60)
