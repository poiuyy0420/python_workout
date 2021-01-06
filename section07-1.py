# Section07-1
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스터스 변수

# 클래스, 인스턴스 차이 중요
# 네임스페이스 : 객체를 인스턴스화 할 떄 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체 보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용

# 선언
# class 클래스명:
#     함수
#     함수
#     함수


# 예제1
class UserInfo:
    # 속성, 메소드
    def __init__(self, name):
        self.name = name
    def usef_info_p(self):
        print("Name : ", self.name)

# 네임스페이스
user1 = UserInfo("Kim")
print(user1.name)
user1.usef_info_p()
user2 = UserInfo("Park")
print(user2.name)
user2.usef_info_p()

print(id(user1))
print(id(user2))
print(user1.__dict__)
print(user2.__dict__)


# 예제2
# self의 이해

class SelfTest:
    @staticmethod
    def function1():
         print('function1 called!')
    def fucntion2(self):
        print(id(self))
        print('function2 called!')
    


self_test = SelfTest()
# self_test.fucntion1()

SelfTest.function1()
self_test.fucntion2()

print(id(self_test))
SelfTest.fucntion2(self_test)


# 예제3
# 클래스 변수, 인스턴스 변수

class WareHouse:
    # 클래스 변수 (모두가 공용으로 사용)
    sotck_num = 0
    def __init__(self, name):
        self.name = name
        WareHouse.sotck_num += 1
    def __del__(self):
        WareHouse.sotck_num -= 1

user1 = WareHouse('Kim')
user2 = WareHouse('Park')
user3 = WareHouse('Kwon')

# 네임스페이스
print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__) # 클래스 네이스페이스, 클래스 변수(공유)

print(user1.name)
print(user2.name)
print(user3.name)

print(user1.sotck_num)
print(user2.sotck_num)
print(user3.sotck_num)

del user1

print(user2.sotck_num)
print(user3.sotck_num)