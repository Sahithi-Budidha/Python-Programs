class person:
    counter=0
    def __init__(self, a='Sahi', b='Female'):
        self.name=a
        self.gender=b
        person.counter=person.counter+1
    def showinfo(self):
        print("Name:",self.name)
        print("Gender:",self.gender)
    @classmethod
    def showcount(cls):
        print("Number of obj created so far:",cls.counter)
