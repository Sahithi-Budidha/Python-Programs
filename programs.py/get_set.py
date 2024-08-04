#before _ (it is public)
'''class car:
    def __init__(self,a=40):
        self.speed=a
    def get_speed(self):
        return self.speed
    def set_speed(self,a):
        self.speed=a
        return'''
#after_ it is now private
'''class car:
    def __init__(self,a=40):
        self._speed=a
    def get_speed(self):
        return self._speed
    def set_speed(self,a):
        self._speed=a
        return'''
#if wrong values is assigned, can stop it by adding conditions such as:

class car:
    def __init__(self,a=40):
        self.set_speed(a)
    def get_speed(self):
        return self._speed
    def set_speed(self,a):
        if a<=0 or a>=160:
            print("Speed needs to be between 0 to 160")
        else:
            self._speed=a
      









