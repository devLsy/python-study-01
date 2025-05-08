# 튜플
# food1 = ("피자", "햄버거", "치킨", "라면", "된장찌개")
# 리스트
# food2 = ["피자", "햄버거", "치킨", "라면", "된장찌개"]

# print(type(food1))
# print(type(food2))

# print(food1[0])

# 리스트는 아래처럼 인덱스에 해당되는 요소의 값 변경 가능함
# food2[0] = "김치"
# print(food2)
# 아래처럼 튜플에서 작업할 경우 에러 발생
# 값을 수정할 수 없음, 튜플은 요소의 값을 변경할 수 없다는 점을 제외하고 리스트와 같음
# food1[0] = "김치"
# print(food1)

# 튜플을 2개로 나눔
food1 = ("피자", "햄버거", "치킨")
food2 = ("라면", "된장찌개")

food3 = food1 + food2
print(food3)
print(len(food3))
print(food3 * 3)


