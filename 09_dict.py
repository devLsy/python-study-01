# 딕셔러니(키쌍 조합)
# user = {"name": "ironMan", "job": "프로그래머", "email": "ironMan@gmail.com"}

user = {"name": "hulk",
        "job": "developer",
        "email": "hulk@naver.com",
}
print(user)
# 사용법(키로 접근)
# print(user["name"])
user["power"] = 300

# del user["job"]

print(user)
# 요소 추가
user["age"] = 15
print(user)
# 요소 삭제
# del user["job"]
# print(user)

# 키만 추출
# keys_list = user.keys()
# 리스트로 변형
# keys_list = list(keys_list)

# print(type(keys_list))
# print(keys_list)
# 값만 추출
# value_list = user.values()
# 리스트로 변형(append나 insert를 사용하려면 변환 필요)
# value_list = list(value_list)
# print(type(value_list))
# print(value_list)

# 값+쌍 조합 추출(리스트안에 튜플이 있는 형태)
item_list = user.items()
# 리스트로 변형
item_list = list(item_list)
# print(item_list)
# print(type(item_list))
# print(item_list[0])
# print(type(item_list[0]))

