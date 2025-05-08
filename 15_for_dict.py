# 딕셔너리에 반복문 사용
user_data = {"name": "ironMan",
             "age": 55,
             "power": 300,
             "email": "ironMan@gmail"
}

# 1번
# for data in user_data:
    # 키만 출력
    # print(data)
    # 키로 값 출력
    # print(user_data[f"{data}"])
    # 키값 모두 출력
    # print(f"{data}: {user_data[data]}")

# 2번(키값 쌍으로 출력)
for data in user_data.items():
    print(f"{data[0]}: {data[1]}")
    # print(data)


