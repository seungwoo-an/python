'''
num={1:'일',2:'이',3:'삼',4:'사',5:'오'}
print("변경 전 값 : ",num)
print()
print("num.setdefault(9) : ",num.setdefault(9,"구우"))#key값 존재 안하면 추가. 존재하면 무시
print()
print("변경 전 후 : ",num)
print()
print("num.get(9)번쨰 value : ",num.get(9))
''''''
num={1:'일',2:'이',3:'삼',4:'사',5:'오'}
aaa={6:'육',7:'칠',8:'팔'}
print('update 전 num : ',num)
num.update(aaa)#num에 aaa를 추가
print('update 후 num : ',num)
''''''
dic={}
ls=[]
ls.append(input("등록할 키값 입력 : "))
ls.append(input("등록할 키값 입력 : "))
ls.append(input("등록할 키값 입력 : "))
#tp='빨강','파랑','노랑'
#dic = dic.fromkeys(tp,ls)
dic = dic.fromkeys(ls)
print("dic키 설정 : ",dic)
dic = dic.fromkeys(ls,0)
print("dic키&값 설정 : ",dic)
''''''
num={1:'일',2:'이',3:'삼',4:'사'}
print("pop 전 num : ",num)
print("\npop(3)실행 : ",num.pop(3))#list 와 달리 최소 1개의 key값이 들어가있어야 함
print("\npop(3)실행 후 num : ",num)
''''''
info={};pe=[];bl=True;num=0
while bl:
    print("1. 인적사항 등록");print("2. 검색");print("3. 종료");
    num=int(input(">>> "))
    if num==1:
        pe=[]
        pe.append(input("이름 입력 : "))
        pe.append(input("점수 입력 : "))
        info.setdefault(pe[0],pe[1])#같은 이름 배제시키는 코드 작성해봐야함(info의 key에 pe[0]이 있으면 안되도록)
    elif num==2:
        name=input("찾고자 하는 학생 이름 입력 : ")
        if info.get(name)==None:
            print("찾고자 하는 학생이 없습니다.")
        else:
            print(name,"님 점수 : ",info.get(name))
    elif num==3:
        print("프로그램을 종료합니다.")
        bl=False
'''
#set(집합)
#저장순서 x, 중복 값 x, 처리하는 순서 x
'''
names={'허준','신사임당','권율','홍길동','허준'}
print(type(names))
print(len(names))
print(names)
''''''
s={}#dict초기화
a=set({})#set초기화
print(type(s))
print(type(a))
print(set('programming'))#중복 허용 x
print(set([12,15,17,11,15]))
dic={'a':1,'b':2,'c':3}#key값만 가져
print(set(dic))
''''''
for x in {'가','나','다','라'}:
    print(x)
'''
#set 조작함수
#변수.add()
#변수.update() - 결합
#변수.remove()
'''
asia={'korea','china','japan'}
print(asia)
asia.add('thailand')
print(asia)
asia.add('china')
print(asia)
asia.remove('japan')
print(asia)
''''''
asia={'korea','china','japan'}
print(asia)
asia2={'iraq','singapore','korea'}
asia.update(asia2)
print(asia)
print('-'*40)
asia={'korea','china','japan'}
asia2={'iraq','singapore','korea'}
#asia3=asia+asia2   -   set끼리 +할 수 없음
#print(asia3)
'''
'''
#집합의 연산
1. 합집합(|) : 두 집합의 전체 요소들의 모음
2. 교집합(&) : 두 집합의 공통 요소들의 모음
3. 차집합(-) : 왼쪽 집합의 요소에서 오른쪽 집합의 요소 제거
4. 배타적 차집합(^) : 합집합-교집합
5. 부분집합(<=) : 왼쪽 집합이 오른쪽 집합의 부분집합인지의 여부를 확인(T/F 반환)
6. 진성 부분집합(<) : 부분집합이면서 추가로 요소가 더 존재하는지를 확인(T/F 반환)

*부분집합과 진성 부분집합의 차이는 부분집합일 경우는 좌우 집합이 같아도 부분집합이지만
진성부분집합인 경우는 좌우 집합이 모두 같을 경우 성립되지 않는다.
''''''
two={2,4,6,8,10}
three={3,6,9,12,15}
print("교집합 : ",two&three)
print("합집합 : ",two|three)
print("차집합 : ",two-three)
print("배타적 차집합 : ",two^three)
''''''
animal = {'호랑이','사자','강아지','치타','햄스터','고양이'}
pet = {'강아지','고양이','햄스터'}
print(pet<=animal)
print(pet<=pet)
print(pet<animal)
print(pet<pet)
''''''
#문자열
Str='Have a nice day'
print("Str[0] : ",Str[0])
print("Str[1] : ",Str[1])
print("Str[2] : ",Str[2])
print("Str[3] : ",Str[3])
print()
print("문자열의 총 길이 : ",len(Str))
print("Str : ",Str)
print("반복문으로 출력")
for i in Str:
    print(i,end="")
''''''
Str='Have a nice day'
arr=Str[7:11]
print("Str : ",Str)
print("arr : ",arr)
''''''
#한글은 기본 두칸 차지 but 인덱스는 글자당 하나씩
Str = '즐거운 파이썬'
print("Str\t:",Str)
print("Str[0]\t:",Str[0])
print("Str[1:3] :",Str[1:3])
print("Str[3:] :",Str[3:])
print("Str[:3] :",Str[:3])
''''''
Str = 'Have a'
print("변경 전 Str : ",Str)
Str+=' nice day '
print("변경 후 Str : ",Str)
print("Str*3 : ",Str*3)
'''
#문자열 함수
'''
str.upper()
str.lower()
str.swapcase() - 대,소문자 상호 변경
str.title() - 각 단어의 앞 글자만 대문자로 변경
''''''
Str='Python is Easy. 그리고 programming 할만하다^^'
print("Str : ",Str)
print()
print("Str.upper() : ",Str.upper())
print()
print("Str.lower() : ",Str.lower())
print()
print("Str.swapcase() : ",Str.swapcase())
print()
print("Str.title() : ",Str.title())
'''
#Str = Str.lower()등으로 저장해주어야 바뀜
'''
a='a'
a.upper()
print(a)# a 나옴
''''''
#Str.title() :영단어만 따로 분리해서 그 단어의 앞 글자를 대문자로, 나머지 소문자로
st='NevEr-eVer110gIVe up'
st=st.title()
print(st)
'''
#문자열 찾기
'''
Str.count() - 찾을 문자열의 갯수
Str.find() - 찾을 문자열의 위치, 없으면 -1
Str.rfind() - 뒤에서부터 찾음
Str.index() - 없으면 error
''''''
st='Have a nice day'
print("st : ",st)
print()
print("st안에 'a'문자 갯수 : ",st.count('a'))
print("st안에 'day'문자 갯수 : ",st.count('day'))
print("st안에 'dak'문자 갯수 : ",st.count('dak'))
''''''
st = 'It is a fun Python class'
print("총 갯수 : ",len(st))
print("a 갯수 : ",st.count('a'))
print("s 갯수 : ",st.count('s'))
''''''
st='Have a nice day'
print("st : ",st)
print("find: 'day'위치 : ",st.find('day'))
print("index: 'day'위치 : ",st.index('day'))
print("find: 'kkk'위치 : ",st.find('kkk')) #없을 경우 -1 반환
print("index: 'kkk'위치 : ",st.index('kkk')) : #없을 경우 오류
''''''
st='Have a nice day'
print("st : ",st)
print("find : 'a'위치 : ",st.find('a'))
print("find : 'a'위치 : ",st.find('a',2))
print("find : 'a'위치 : ",st.find('a',6))
print("find : 'a'위치 : ",st.find('a',14))#,값 -> 해당 인덱스 이후로 탐색
'''
