# factory: creational dp
# hides logic of creating object

from abc import ABCMeta, abstractmethod

class Person(metaclass=ABCMeta):
    @abstractmethod
    def create(self):
        pass

class HR(Person):
    def create(self, name):
        print(f"HR {name} is created")

class Engineer(Person):
    def create(self, name):
        print(f"Engineer {name} is created")

class PersonFactory(object):
    @classmethod
    def create(cls, type, name):
        eval(type)().create(name)

def main():
    hr = PersonFactory.create("HR", "dhruv")
    eng = PersonFactory.create("Engineer", "dhruv")


if __name__ == "__main__":
    main()
