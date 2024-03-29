'''
0b : 2진수
0o : 8진수
0x : 16진수 (10~15는 알파벳사용)
'''
'''
print(0b01111011)

print(0o173)

print(0x7b)

print(123)

# 기본적으로 10진 정수로 표현됨
'''
'''

print("2진수:",bin(0b01111010))

print("8진수:",oct(0b01111010))

print("16진수:",hex(0b01111010))

print("10진수:",0b01111010)

'''
'''
서식제어문(문자열 밖에 있는 숫자를 가져옴/앞에 %를 써줘야함/단앞에 )
%d : 10진 정수
%o : 8진 정수
%x : 16진 정수

'''
'''
print("%d"%123)

#print("%d%d"%123)

#print("%d"%(123,321))

print("%d%d"%(123,321))

print("%d+%d=%d"%(123,321,123+321))

print("%d"%123,321)
'''
'''
print("10진 정수:%d"%123)
print("10진 정수:%d"%0o173)
print("10진 정수:%d"%0x7b)

print("8진 정수:%o"%123)
print("8진 정수:%o"%0o173)
print("8진 정수:%o"%0x7b)

print("16진 정수:%x"%123)
print("16진 정수:%x"%0o173)
print("16진 정수:%x"%0x7b)
'''
'''
print("정수 표현 : %d"%123)
print("정수 표현 : %d"%123.123) # 정수만 표현(소수점 아래는 버림)
print("정수 표현 : %d %d"%(123,456))

print("\n실수 표현 : %f"%456) # 소수점 여섯째 짜리 까지 표현
print("실수 표현 : %f"%456.456) # 쇼트 : 6째자리까지 / 더블 : 15째자리까지
print("실수 표현 : %f %f"%(456.456,123.123))
'''
'''
print(" 문자 표현 : %c %c"%("한","글")) # %c : 단일 문자
print(" 문자 표현 : %c %c"%('표','현'))
print("\n 문자열 표현 : %s"%"안녕") # %s
print(" 문자열 표현 : %s\t%s"%("문자열",'표현방식'))
#print("%c %c"%(97,65) >>> a A  아스키코드
'''
'''
#별다셧개 매우중요

print("기본 값 :%d"%123)
print("기본 값 :%         d"%123) # escape 문자는 안됨
print("설정 값 :%5d"%123) # %숫자d > 숫자만큼 칸 확보
print("설정 값 :%05d"%123) # 05 > 빈칸에 0 채움(-05는 존재하지 않음)
print("설정 값 :%5d%5d"%(123,123))
print("설정 값 :%-5d%-5d"%(123,123)) # 양수 칸내에서 우측정렬, 음수 칸내에서 좌측정렬
'''
'''

# 이것도 중요

print("기본 값 :%f"% 123.45678)

print("설정 값 : %10.3f"%123.45678) # 정수 > 소수점,소수를 포함한 칸확보 , 소수점 뒤 숫자 > 확보할 소수점자리수

print("설정 값 :%2.1f"%123.45678) # 많으면 칸 확보가 무시됨

print("설정 값 :%.2f"%123.45678) # 보통 이렇게 사용(반올림)

'''
'''
print("123456123456123456123456123456123456")
print("%6s%6s%6s"%('대한','민국','만세')) # 서식제어문에서 한글은 정렬이 힘듬(\t는 visual code에서는 정렬 잘됨)
print("기본 값 :%s"%"python test")

print("설정 값 :%20s"%"python test")
'''
'''
print("================출력결과===================")
print("이름 : %s"%"홍길동")
print("나이 : %d"%20)
print("Tel : %03d-%d-%d"%(10,1234,1234))
print("키 : %.1f"%178.5)
print("몸무게 : %d"%75)
print("혈액형 : %s"%"O")

print()
print("================출력결과===================")
print("이름 : %s"%"홍길동")
print("나이 : %d"%20)
print("Tel : %s-%s-%s"%("010","1234","1234"))
print("키 : %.1f"%178.5)
print("몸무게 : %d"%75)
print("혈액형 : %s"%"O")

print()
print("================출력결과===================")
print("이름 : %s"%"홍길동")
print("나이 : %d"%20)
print("Tel : %s"%"010-1234-1234")
print("키 : %.1f"%178.5)
print("몸무게 : %.0d"%75)
print("혈액형 : %s"%"O")

print()
print("================출력결과===================")
print("이름 : %s"%"홍길동")
print("나이 : %d"%20)
print("Tel : %03.0f-%.0f-%.0f"%(10,1234,1234))
print("키 : %.1f"%178.5)
print("몸무게 : %d"%75)
print("혈액형 : %s"%"O")

print()
print("-답안-")
print("이름 \t: %s"%"홍길동")
print("%-5s %-10s"% ("이름",": 홍길동"))
print("나이 \t: %d"%20)
print("나이 \t: %s"%"20")

print("Tel \t: %s"%"010-1234-1234")
print("Tel \t: 0%d-%d-%d"%(10,1234,1234))
print("Tel \t: %03d-%d-%d"%(10,1234,1234))

print("키 \t: %.1f"%178.5)
print("몸무게 \t: %d"%75)
print("혈액형 \t: %s"%"0")
'''
'''
변수 : 값이 고정되어 있지 않고 변하는 수 <> 상수 : 항상 고정되어 있는 값
변수란? 한가지 값으로 고정되지 않고 여러 가지 값으로 변할 수 있는 공간
-> 데이터를 사용하기 위해 메모리에 공간을 할당 받는데 할당 받은 공간에 이름을 정해 두고 원할 때 꺼내 쓰거나, 변경 할 수 있음
상수는 재활용할 수가 없음

변수명 작명 규칙(이거 안지키면 에러남)
- 변수의 이름은 알파벳, 숫자, 언더바(_)로 구성
- 대소문자 구분
- 변수의 이름은 숫자로 시작할 수 없음
- 키워드(예약어)는 변수이름으로 사용 불가능
예약어란? 프로그래밍 언어 중에서 의미가 고정되어 있고, 사용자가 작성하는 프로그램 상태에 따라서 의미를 변경할 수 없는 단어
ex) print
- 공백이나 특수 기호는 포함될 수 없음

변수 작명 요령
1) 변수는 그 프로그램 내부에서 어떠한 기능을 하는지
   또는 어떠한 데이터를 담을건지 누구나 쉽게 연상할 수 있도록 지어주는 것이 좋다
    예) 이름 data = name
2) 한글 변수 사용 가능... 그러나 한글변수는 가급적 사용하지 말자
   한글은 한국 사람나의 고유문자... 외국인은 알아보기 쉽지 않습니다.
   현시대에 오픈소스가 대세인데 다른 외국인들은 한글 변수를 알아보기가 힘듭니다.
   그래서 가급적 한글 변수사용은 피해야 합니다.
'''
'''
num=100 # A=B : B를 A에 대입하다(A: 변수 가능, 상수 불가능, B: 변수, 상수, 연산식 가능)

print("정수 형 변수 사용 : %d"%num)

print("정수 형 변수 사용 : ",num)

print("정수 형 변수 사용 : num") # 이럴 경우 num 이 나옴

'''
'''
# 굉장히 중요

num=5

print("변경 전 num : ",num)

num = num + 10

print("변경 후 num : ",num)
'''
'''
num1 = 5
num2 = 10
sum_ = num1+num2
print("id num1 : ",id(num1)) # id: 객체의 중복성을 확인하기 위한 일련번호
print("id num2 : ",id(num2))
print("id sum : ",id(sum_))
print(id(15))
'''
'''
num1 = 10
num2 = 20
sum_ = 30

print("num1(",num1,") + num2(",num2,") = ",sum_)

# 답안

print("num1(%d)+num2(%d)=%d"%(num1,num2,num1+num2))
print("num1(",num1,")+num2(",num2,")=",num1+num2) # ,를 쓰면 한칸씩 띄어쓰기됨

'''





      
