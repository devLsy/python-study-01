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

class User:
    def __init__(self, user_info):
        self.__dict__.update(user_info)
        # self.name = user_info["name"]
        # self.age = user_info["age"]
        # self.job = user_info["job"]
        # self.power = user_info["power"]
        # print(f"이름: {self.name}\n나이: {self.age}\n직업: {self.job}")
        # print(f"{self}")
    def __str__(self):
        return ", ".join(f"{key}: {value}" for key, value in self.__dict__.items())

    def print_info(self):
        print(f"======= {self.name} info ======")
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")

user1_data = {"name": "고길동", "age": 60, "job": "개발자", "power":100}
user2_data = {"name": "홍길동", "age": 40, "job": "기획자", "power": 300}

go = User(user1_data)
ho = User(user2_data)

go.print_info()
ho.print_info()

go.__str__()
ho.__str__()

print(go)