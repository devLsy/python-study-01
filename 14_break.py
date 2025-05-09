# 브레이크, 컨티뉴
count = 1
#
while count < 11:
    print(f"{count}바뀌째")
    count += 1
    if count >= 11:
        break
        # continue
print("달리기 끝")

# count = 0
#
# while True:
#     count += 1
#     if count == 19:
#         print("좀 쉬어야겠다..")
#         continue
#     print(f"{count}바뀌째")
#     if count == 20:
#         break
# print("달리기 끝")

print("=========================")

for i in range(20):
    if i == 5:
        print("좀 쉬자")
        continue
    print(f"{i}바뀌 째 돌았다.")
print("달리기 끝")