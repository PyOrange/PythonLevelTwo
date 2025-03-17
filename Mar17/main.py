'''
클래스 기능 실험하는 메인 클래스
'''
from Practice.Person1 import Person1

print(Person1.__doc__)

per1 = Person1("Orange", 10)
per2 = Person1("Neon", 102)

personList1 = []

personList1.append(per1)
personList1.append(per2)

for i in personList1:
    print(Person1.count)
    print(personList1)
    print(Person1.getinfo)

print(per1.name == per2.name)

Person1.getinfo(per1)

for a in personList1:
    print(str(a))
    

for x in range(5):
    print(per1.getinfo2())

