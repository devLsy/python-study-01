# 내장 함수
name = input("이름을 입력하세요 : ")
print(f"{name}, len: {len(name)}")

print(type(int("1234")))
print(type(str(1345)))

# range를 이용해서 list 만들기
temp = list(range(1, 11))
print(temp)

num = [1, 100, -9, 54, -4]
print(sorted(num))
print(sorted(num, reverse=True))
# 문자열에도 max, min   사용 가능
num = ["A", "z", "t", "u", "Y"]
# num = "asdaTAZF"
print(max(num))
# print(min(num))

