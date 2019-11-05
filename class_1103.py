'''
txt = 'working env at ebi is great'
words = txt.split()
#튜플 리스트 생성, 각 튜플은 단어 앞에 길이 정보를 가진다.
t=list()
for word in words:
    t.append((len(word),word))
print(t)
t.sort(reverse=True)
print(t)
#튜플 리스트를 운행하여 훑고 길이에 따라 내림차순으로 단어 리스트 생성
res=list()
for length, word in t:
    res.append(word)
print(res)
''''''
t=(1,2,3)
c_t=t
print(c_t)
print(t)
c_t+=4,5
print(c_t)
print(t)
''''''
#dictionary
student = {'학번':1234,"이름":"홍길동","학과":"IT학과"}
print(student)
mobile={"품명":"갤럭시","가격":100,"크기":10}
print(mobile)
''''''
impo={}
impo['파이썬']='www.python.org'
impo['네이버']='www.naver.com'
impo['구글']='www.google.org'
print("파이썬 : ",impo['파이썬'])
print("네이버 : ",impo['네이버'])
print("구글 : ",impo['구글'])
print(impo)
''''''
impo={}#{key, value}
name=input('키값 입력:')
val=input('값 입력:')
impo[name]=val
print(name,":",impo[name])
''''''
dict={}
#import collections
#dict=collections.OrderedDict() - 순서 있는 dict(ver 3.4이전)
for i in range(5):
    key=input("이름(key) 입력 : ")
    value=input("값(value) 입력 : ")
    dict[key]=value
print(dict)
print(dict.keys())
'''
#dic.keys() - key값 출력
#dic.values() - value 출력
#dic.items() - key와value를 tuple로
#dic.clear() - 초기화(list에서도 사용 가능)
#dic.get(key) - key값 가져옴
#dic.setdefault(키,값)- key가 없으면 추가 설정
#dic.update(obj) - 다른 사전의 내용으로 갱신
#dic.pop(key) - key에 해당하는 값을 지움
#dic=dic.fromkeys(키) or (키,값) - (key,value)리스트나 튜플로 설정
'''
num={1:'일',2:'이',3:'삼',4:'사'}
print("num.keys() : ",num.keys())
print()
print("num.values() : ",num.values())
print()
print("num.items() : ",num.items())
print()
print("num.get(1) : ",num.get(1))
print()
''''''
num={1:'일',2:'이',3:'삼',4:'사'}
print("num.keys() : ",num.keys())
print("list(num) : ",list(num))#key값만 리스트화
print("list(num.keys()) : ",list(num.keys()))
print()
print("num.values() : ",num.values())
print("list(num.values()) : ",list(num.values()))
''''''
singer={}
singer['이름']=input("가수 이름 입력 : ")
singer['구성원']=input("인원 수  입력 : ")
singer['대표곡']=input("대표 곡  입력 : ")
#반복문의 매개변수에 key값 대입
for i in singer.keys():
    print("%s : %s"%(i,singer[i]))
''''''

''''''
num={1:'일',2:'이',3:'삼',4:'사',5:'오'}
print(num)
print("num.get(3) : ",num.get(3))
print("num.get(9) : ",num.get(9))
print("num.get(0) : ",num.get(0,'없음'))
su = int(input("찾고자 하는 key 입력 : "))
if num.get(su)==None:
    print("값이 없습니다.")
else:
    print(num.get(su))
''''''
#네비게이션 만들기
navi={};bl=True;num=0
while bl:
    print("="*30)
    print("1.목적지 등록");print("2.목적지 수정");print("3.목적지 검색");print("4.목적지 삭제");print("5.목적지 목록");print("6.종료")
    num=int(input(">>>"))
    if num!=1 and num!=2 and num!=3 and num!=4 and num!=5 and num!=6:
        print("="*30)
        print("잘못 입력하셨습니다.")
        continue
    elif num==1:
        des=input("목적지 입력 : ")
        if navi.get(des)!=None:
            print("="*30)
            print("이미 등록된 목적지입니다.")
            continue
        navi[des]=input("목적지 주소 입력 : ")
    elif num==2:
        if navi=={}:
            print("="*30)
            print("검색할 목적지가 없습니다.")
            continue
        des=input("검색할 목적지 입력 : ")
        if navi.get(des)==None:
            print("="*30)
            print(navi.get(des,'검색할 목적지가 없습니다.'))
            continue
        print(des,":",navi[des])
    elif num==3:
        if navi=={}:
            print("="*30)
            print("수정할 목적지가 없습니다.")
            continue
        des=input("수정할 목적지 입력 : ")
        if navi.get(des)==None:
            print("="*30)
            print(navi.get(des,'수정할 목적지가 없습니다.'))
            continue
        navi[des]=input("수정할 목적지 주소 입력 : ")
    elif num==4:
        if navi=={}:
            print("="*30)
            print("삭제할 목적지가 없습니다.")
            continue
        des=input("수정할 목적지 입력 : ")
        if navi.get(des)==None:
            print("="*30)
            print(navi.get(des,'삭제할 목적지가 없습니다.'))
            continue
        navi.pop(des)
    elif num==5:
        if navi=={}:
            print("="*30)
            print("등록된 목적지가 없습니다.")
            continue
        for i in navi.keys():
            print(i,":",navi[i])
    elif num==6:
        print("="*30)
        print("네비게이션을 종료합니다.")
        bl=False
''''''
student={'학번':1234,'이름':'홍길동','학과':'IT학과'}
print(student['학번'])
print(student['이름'])
print(student['학과'])
print()
print(student.items())
print()
print(student)
''''''
name={'이순신':'거북선','세종대왕':'훈민정음','파이썬':'프로그래밍 언어'}
for key,value in name.items():
    print(key,":",value)
#for key in name.keys():
    #print(key,":",name[key])
print("삭제 : ",name.clear())
print("삭제 후 값 : ",name)
'''
