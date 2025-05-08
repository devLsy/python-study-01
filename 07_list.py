# 리스트(서로 다른 데이터 타입을 넣을 수도 있음)
# 리스트 안에 리스트를 넣을 수도 있음
food0 = ["김치", "삼겹살", "김치", "포도"]
tmp = ["g", "a", "T", "p"]
# food0.append("피자")
print(food0)
# 원하는 인덱스에 추가
# food0.insert(1, "피자")
# print(food0)

# 요소 삭제(여러개 있으면 제일 처음 요소만 삭제("김치"가 3개 있을 때 remove를 실행하면 제일 처음의 김치만 삭제됨))
# food0.remove("김치")
# print(food0)
# 인덱스 찾기
# print(food0.count("김치"))
# 몇번 째 인덱스에 있는지
# print(food0.index("김치"))
# 오름차순 정렬
# food0.sort()
# print(food0)
# 내림차순 정렬
# food0.sort(reverse=True)
# print(food0)

# print(tmp)
# 0번 째 인덱스 요소의 값 변경
# tmp[0] = "피자"
# print(tmp)


# food1 = [100, "삼겹살", "감자튀김"]
# food2 =  ["피자", "햄버거"]
# food3 = food1 + food2
# food4 = food1 * 3

# print(food1)
# print(food2)
# print(food3)
# print(food4)



# print(type(food1))

# print(len(food1))
# print(food1[0])
# print(food1[0:2])
# print(type(food1[0]))
# print(food1[1][0])

food1 = ["아이언맨","토르","헐크","로키","블랙 위도우"]
print(food1.count("아이언맨"))
food1.insert(1, "굿")
print(food1)
food1.remove("굿")
print(food1)
print(food1.index("헐크"))
food1.sort(reverse=True)
print(food1)