#print("hello")
'''
print("python 첫날 입니다")#줄주석은 #기호를 사용합니다

블럭주석은 보고서 형태 / 미리 준비 /
자기가 만든 코드는 삭제 금지(틀렸으면 왜 틀렸는지 분석)
print("python을# 시작해 볼까요")


print("hello")

print("python 첫날 입니다")

print("python을 시작해 볼까요")
'''

'''
print("쌍다옴표 안의 내용 출력");print("이어 쓰기 실행")

print("이어쓰기"); print(); print(";(쎄미콜론이라고 읽는다)")
'''

'''
================ RESTART: E:/10월_파이썬기초_1900_강혜선/class_1018.py ================
쌍다옴표 안의 내용 출력
Traceback (most recent call last):
  File "E:/10월_파이썬기초_1900_강혜선/class_1018.py", line 17, in <module> >이러한 모듈안에, 14번째 줄에서
    print("쌍다옴표 안의 내용 출력");a+b;print("이어 쓰기 실행") > 여기서 에러가 났다
NameError: name 'a' is not defined > 변수에 대한 에러명 / a 라는 변수가 정의 되지 않음
한줄에 한오더씩 해야 알아보기 편함
'''

'''
ESCAPE 문자(문자열 안에 사용)
\n : 새로운 줄로 이동
\t : 탭크기만큼 이동(1칸이라도 남을때까지 8칸씩 확보, 주로 정렬할때 사용)
\" : "출력함
\' : '출력함
'''

'''
print("Hello Python");

print("Hello \nPython");

print("재밌는");print("Python")
'''

'''
print("Hello" #문자열은 한 행에서 시작해서 끝나야한다. 따옴표가 두개다 한줄에 있어야함
      " Python" # 따옴표 세 개를 쓰면 엔터쳐도 문자열이 이어짐
      " Start")

print("Hello\n"
      " Python\n"
      " Start")
'''

'''
print("저의 이름은 홍길동 입니다")
print("저의 나이는 20살 입니다")
print("주소는 산골자기 입니다")
print()
print("저의 이름은 홍길동 입니다\n"
      "저의 나이는 20살 입니다\n"
      "주소는 산골자기 입니다")
print()
print("저의 이름은 홍길동 입니다\n저의 나이는 20살 입니다\n주소는 산골자기 입니다")
'''

'''
print("123456781234567812345678123456781234567812345678")
print("Have\t"
      "a\t"
      "Good\t"
      "Time.")
print("1234567\t"
      "1\t"
      "12345678\t"
      "123")
print("대한민국\t만세\t대한독립만세\t만만세\t") #한글은 2칸 확보(2bite)
'''

'''
print("쌍 따옴표\"")

print("홋 따옴표'")

print('쌍 따옴표"')

print('홋 따옴표\'')
'''

'''
print('표현 \ 방식')
print('표현 \2 방식') # \2 특수문자로 나타남(아스키코드표참조)
print('표현 \\2 방식') # 금액 표시 할 때 사용 \\ -> \
#print('표현 방식\') #error code
print('표현 방식\\')
'''

'''
print("=====================\n"
      "\t /)/) \n"
      "\t(  ..)\n"
      "\t(  >♡\n"
      "  Have a Good Time.  \n"
      "=====================")
print()
print()
print("\t\t####회비 정보####\n"
      "==================================================\n"
      "이름\t\t나이\t전화번호\t\t회비\n"
      "==================================================\n"
      "홍길동\t\t\"15\"\t010-123-1234\t\\20,000\n"
      "임꺽정\t\t\"20\"\t010-234-2345\t\\30,000\n"
      "김말이\t\t\"28\"\t010-345-3456\t\\50,000\n"
      "--------------------------------------------------\n"
      "총합계\t\t\t\t\t\\100,000\n"
      "==================================================\n")
'''

'''
print(123 + 123)

print(542 - 242)

print(2 * 123)

print(120 / 3)
'''

'''

print("덧셈 결과 : ",123 + 123) # 숫자는 구분하기 위해 , 사용

print("뺄셈 결과 : ",542 - 242)

print("곱셈 결과 : ",2 * 123)

print("나눗셈 결과 : ",120 / 3) # 파이썬은 나눗셈을 하면 실수형으로 나옴 그래서 소수점첫째자리가 보임 

'''

print("12 + 54 = ",12+54," 입니다")
      
print("268 - 42 = ",268-42," 입니다")

print("2 * 23 = ",2*23," 입니다")

print("120 / 3 = ",120/3," 입니다")


