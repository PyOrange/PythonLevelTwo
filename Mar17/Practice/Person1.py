class Person1():
    '''
    연습용 사람 클래스1
    '''
    count = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person1.count += 1
    
    def __str__(self):
        return "info : {} - {}".format(self.name, self.age)
    
    def getinfo(self):
        return("id : {}".format(id(self)))

    def getinfo2(self):
        return "name : {}, age : {}".format(self.name, self.age * Person1.count)