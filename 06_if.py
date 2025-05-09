#조건문
today = "일요일"
payday = 30

if today == "월요일":
    print("출근해야지.")
elif today == "일요일":
    print("오늘은 쉬는날~!")
else:
    print("무슨요일이지?")

print("================================ ")

if payday < 30:
    print("아직 돈이 안 들어왔음")
elif payday == 30:
    print("월급 입금 됨")
else:
    print("무슨요일이지?")

print("================================ ")

pizza = True
# 파이썬에서는 아래처럼 비어있는 변수는 False로 인식한다고 함
pizza = ""
pizza = " " # 이것은 빈 문자열이 있으므로 True로 인식
pizza = 1 # 숫자는 0이 아닌 경우는 전부 True
hamburger = False
# or과 and로 논리 연산처리
if pizza or hamburger:   # or 또는 and로 논리 연산처리
# if not pizza:   # 반대로(피자가 True가 아닌 경우)
    print("피자 또는 햄버거가 있다.")
elif hamburger:
    print("햄버거가 있다.")
else:
    print("아무것도 먹을게 없다.")
