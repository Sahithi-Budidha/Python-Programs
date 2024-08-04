#creating a class
'''class person:
    name='sahi'
    gender='female'
    def showinfo(self):
        print("Name:",self.name)
        print("Gender:",self.gender)'''
#now creating a class with __init__() in it.
class person:
    def __init__(self, a='Sahi', b='Female'):
        self.name=a
        self.gender=b
    def showinfo(self):
        print("Name:",self.name)
        print("Gender:",self.gender)

