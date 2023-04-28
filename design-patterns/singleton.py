# singleton: creational dp
# provide single instance of class everywhere

class Singleton(object):
    def __new__(clas, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
