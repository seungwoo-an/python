'''
#1.
st='Have a nice day Have a nice day Have a nice day'
result=[]
sum_a=0
for i in range(len(st)):
    if st[i]=='a':
        sum_a+=1
        result.append(i)
print(sum_a)
print(result)
#2.
st='Have a nice day Have a nice day Have a nice day'
result=[]
sum_a=0
for i in range(len(st)):
    if st.find('a',i)==i:
        sum_a+=1
        result.append(i)
print(sum_a)
print(result)
#3.
st='Have a nice day Have a nice day Have a nice day'
result=[]
sum_a=0
while True:
    sum_a=st.find('a',sum_a)
    if sum_a !=-1:
        result.append(sum_a)
        sum_a+=1
    else: break
print(len(result))
print(result)
'''
#문자열 변경
'''
str.strip()- 문자열 양 끝 문자 제거(양쪽 공백 제거)
str.rstrip() - 끝, 공백 제거
str.lstrip() - 처음, 공백 제거
str.replace()
''''''
st='        파 이 썬        '
print(st)
print("st\t\t:{}{}{}".format('*',st,'*'))
print()
print('st.strip()\t:{}{}{}'.format('*',st.strip(),'*'))
print(st)
''''''
st='파이썬파'
print('st\t\t:',st)
print()
print('Str.strip()("파")\t:',st.strip('파'))
print("="*40)
st='파이썬'
print('st\t\t:',st)
print()
print('Str.strip()("파")\t:',st.strip('파'))
print("="*40)
''''''
st='---무---빙---'
print("st\t\t:",st)
print('st.strip("-")\t:',st.strip('-'))
print('st.rstrip("-")\t:',st.rstrip('-'))
print('st.lstrip("-")\t:',st.lstrip('-'))
''''''
st='2015/04/02'
print("st\t\t:",st)
print("replace()\t:",st.replace('/','.'))#/->.으로 치환
print("replace([0:4])\t:",st.replace(st[0:4],'2017'))#2015->2017치환
print("replace([0:4])\t:",st.replace(st[3:4],'7'))
''''''
st="""
오늘 하루도 즐겁게
오늘 하루도 행복하게
오늘 하루도 최선을
"""
print(st)
''''''
#1.
st="""
김개똥 -2017년 03월 24일
홍길동구리 -2015년 04월 02일
선우선녀 -2018년 05월 14일
"""
for i in range(len(st)):
    if st[i]=='-':
        st=st.replace(st[i+1:i+5],'1999')
st=st.replace('-',':')
print(st)
#2.
st="""
김개똥 -2017년 03월 24일
홍길동구리 -2015년 04월 02일
선우선녀 -2018년 05월 14일
"""
for i in range(len(st)):
    if st[i]=='년':
        st=st.replace(st[i-4:i],'1999')
st=st.replace('-',':')
print(st)
#while 문으로도 작성
'''
#문자열 변경
'''
str.split() , str.split('Str')
str.join() 
str.splitlines() - \n단위로 나눔
''''''
st='Never ever give up'
print("st\t\t:",st)
print('st.split()\t',st.split())#공백단위로 나눈 후 리트스
print('st.split()\t',st.split(" "))
''''''
st='하나:둘:셋'
print('st\t\t:',st)
print('st.split(:)\t',st.split(':'))
st='일,이,삼'
print('st\t\t:',st)
print("st.split(,)\t",st.split(','))   
''''''
st='Never ever give up'
print('st:',st)
print("st.splitlines():",st.splitlines())
st="""
Never ever give up
Never ever give up
"""
print("st.splitlines():",st.splitlines())#\n포함 line기준으로 list 생
st='하나\n둘셋'
print("st.splitlines():",st.splitlines())
''''''
#A.join(B) -> A를 B 구성요소 사이 사이에 추가
Str='123'
print('"%".join(123)\t:','%'.join(Str))
print('123.join("%a")\t:',Str.join('%a'))
print("="*50)
li=['','123','456']
print('"공백".join([123,456])\t:',"".join(li))
print("="*50)
li=['','안녕하세여','만나서 반갑습니다.','행복한 하루 되세요']
print('"엔터".join(li)\t',"\n\n".join(li))
'''
#문자열 정렬
'''
str.center()
str.ljust()
str.rjust()
str.zfill()
''''''
Str='Python'
print("Str\t\t:",Str)
print("Str.center(10)\t:",Str.center(10))
print("Str.center(10,'-'):",Str.center(10,'-'))
print("Str.ljust(10)\t:",Str.ljust(10,'-'),Str.ljust(10))
print("Str.rjust(10)\t:",Str.rjust(10),Str.rjust(10,'='))
print("Str.zfill(10)\t:",Str.zfill(10))
''''''
#문제
accountBook="shoes 03/02 59000, coffee 03/03 2500, food 03/04 7000, dress 03/13 130000"
replaceAB= accountBook.split(',')# , 기준으로 리스트 저장
k=0
for i in replaceAB:
    replaceAB[k]=i.lstrip()# 각 문자열의 왼쪽 공객 삭제 후 저장(_coffee,_food,_dress)
    k+=1
kk='$ '
print('item'.ljust(10),end='')
print('date'.ljust(10),end='')
print('$(price)'.ljust(10))
for i in range(len(replaceAB)):
    z=replaceAB[i].split()#공백을 기준으로 리스트로 저장
    for k in range(len(z)):
        if k==0:
            print(z[k].ljust(10),end="")
        elif k==1:
            print(z[k].ljust(10),end="")
        elif k==2:
            print("{:,}".format(int(z[k])).join(kk).ljust(10))
'''
#True or False값 나타냄
#공백, 숫자, 문자 따로 적용
'''
Str='Python te12st 1234'
print("Str.isdigit() : ",Str.isdigit())#숫자로만 구성
print("Str[9:11].isdigit() : ",Str[9:11].isdigit())
print("="*60)
print("Str.isalpha() : ",Str.isalpha())#글자로만 구성
print("Str[:6].isalpha() : ",Str[:6].isalpha())
print("="*60)
print("Str.isalnum() : ",Str.isalnum())#글자 + 숫자 구성
print("Str[7:13].isalnum() : ",Str[7:13].isalnum())
print("="*60)
print("Str.islower() : ",Str.islower())#소문자
print("Str.isupper() : ",Str.isupper())#대문자
print("Str.isspace() : ",Str.isspace())#공백
'''
info="""
jo 9abc08-3022023
cho 900402-1011232
test 1234567-1234567
lee 980908-3a2b0c3
kim 900514-2022023
"""
#주민번호 뒷자리 '*'로 치환하기
'''
print(info)
k=0
for i in range(info.count('-')):
    k=info.find('-',k+1)
    if info[k+1:k+8].isdigit() and not info[k-7:k].isdigit() and info[k-6:k].isdigit():
        info=info.replace(info[k+1:k+8],'*******')
print(info)
'''
