class _Fruit:
    def __init__(self, name: str):
        self.name = name


class _CitrusFruit(_Fruit):
    pass


def _eat(fruit):
    if isinstance(fruit, _CitrusFruit):
        print(f"Eating citrus fruit: {fruit.name}")
    elif isinstance(fruit, _Fruit):
        print(f"Eating fruit: {fruit.name}")


_banana = _Fruit("banana")
_orange = _CitrusFruit("orange")

_eat(_banana)
_eat(_orange)


class Fruit:
    def __init__(self, name: str):
        self.name = name

    def eat(self):
        print(f"Eating fruit: {self.name}")


class CitrusFruit(Fruit):
    def eat(self):
        print(f"Eating citrus fruit: {self.name}")


def eat(fruit: Fruit):
    fruit.eat()


banana = Fruit("banana")
orange = CitrusFruit("orange")
eat(banana)
eat(orange)
