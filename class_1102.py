'''
#2차원 리스트
#ls = [i for i in range(3) for j in range(5)]
#print(ls)
aa=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
for i in range(3):
    for j in range(4):
        print("a[{}][{}] = {}".format(i,j,aa[i][j]))
print("="*40)
for i in range(len(aa)):
    for j in range(len(aa[i])):
        print("a[{}][{}] = {}".format(i,j,aa[i][j]))
print("="*40)
for i in aa:
    for j in i:
        print(j,end="\t")
ls = [[0 for rows in range(3)]for cols in range(5)]
#ls = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
''''''
aa=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
a=aa[0]
a[1]=2000
print("aa[0] : ",aa[0])
print("a : ",a)
print("aa : ",aa)
''''''
from copy import deepcopy as deep
aa=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
a=deep(aa)
print(a)
''''''
ls_1=[]
value=1
for i in range(3):
    ls_2=[]
    for j in range(4):
        ls_2.append(value)
        value+=1
    ls_1.append(ls_2)
print("ls_1 : ",ls_1)
for i in range(len(ls_1)):
    for j in range(len(ls_2)):
        print(ls_1[i][j],end="\t")
    print()
''''''
be = ['2019','12','31']
print(be)
af1=list(map(int,be))#map(A,B) - B:반복할 수 있는 자료형(리스트, 튜플, 셋, 문자열)
                    #           A:반복 처리한 함수(내장, 외장, 사용자정의함수)
af2=tuple(map(int,be))
af3=set(map(int,be))
print(af)
''''''
be=[['100'],['200'],['300']]
print("수정 : ",be)
for i in range(len(be)):
    be[i] = list(map(int,be[i]))
print(be)
for i in range(len(be)):
    be[i][0]=str(be[i][0]*100)
print(" 수정 후 : ",be)
'''
