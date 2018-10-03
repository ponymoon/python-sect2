import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#클래스변수, 인스턴스변수

class nametest:
    total = 0

print(dir())
print("before : ",nametest.__dict__)
nametest.total = 1
print("after : ",nametest.__dict__)

n1 = nametest()
n2 = nametest()
print(id(n1),"vs",id(n2))
print(dir())
print(n1.__dict__)
print(n2.__dict__)
n1.total = 77

print(n1.__dict__)

print(n1.total)
print(n2.total)
