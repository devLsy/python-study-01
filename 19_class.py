# 클래스
class User:
    # 생성자
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job
        print(f"이름: {self.name}. 나이: {self.age}. 직업: {self.job}")

    def hello(self):
        print(f"Hello, my name is {self.name}. I am a {self.job}.")

user1 = User("고길동", 30, "개발자")
user2 = User("홍길동", 25, "디자이너")

user1.hello()
user2.hello()
