days = ["월","화","수","목","금"]
# days = "월화수목금"
# days = "월요일화요일수요일목요일금요일"

for day in days:
    if day == "월":
        print("월요일이네, 일하러 가자.")
    else:
        print(f"{day}요일 입니다.")
        print(f"{day}입니다.")
print("주말이 되었습니다.")

print("===========================")

sum = 0
for i in range(1,11):
    print(i)
    sum += i
print(f"합계: {sum}")

