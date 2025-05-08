# 함수와 리턴
def add(a, b):
    print(f"{a}와 {b}를 입력 받았습니다.")
    print(f"두 값을 더하면 {a+b}입니다.")

    return a + b
# add(1,10)
# add(5,600)

def shopping(items):
    return items
# a = print("hi!!")
# b = input("입력:")
fruits = ["사과", "바나나", "포도"]
print(shopping(fruits))
print(shopping(["사과", "바나나"]))

# print(a)
# print(b)

# 반환값이 없으니 temp는 None
temp = add(1,10)
# add(temp, 100)
# print(temp)

print(f"합은 {temp}")
