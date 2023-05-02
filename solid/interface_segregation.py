from abc import ABCMeta, abstractmethod


class IShape(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        raise NotImplementedError


class Circle(IShape):
    def draw(self):
        pass


class Square(IShape):
    def draw(self):
        pass


class Rectangle(IShape):
    def draw(self):
        pass
