import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#클래스변수, 인스턴스변수

class warehouse:
    stock_num=0
    def __init__(self, name):
        self.name = name
        warehouse.stock_num += 1

    def __del__(self):
        warehouse.stock_num -= 1

user1 = warehouse("kim")
user2 = warehouse("park")

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print(warehouse.__dict__) #인스턴스 네임스페이스 -> 클래스 네임스페이스 , 클래스변수(공유)

print(user1.stock_num)
print(user2.stock_num)
