## SOLID Principles

S - Single Responsibility Principle
<br/>
O - Open/Closed Principle
<br/>
L - Liskov Substitution Principle
<br/>
I - Interface Segmented Principle
<br/>
D - Dependency Inversion Principle

### Single Responsiblity:
   any module should be changed by only one actor
   dont put multiple functionalities in single module
   ```py
    class PasswordHasher:
        def hashAndSavePassword(self, password: str):
            self.hashPassword(password)
            self.savePassword(password)

        def hashPassword(self, password: str):
            print(f"haashing {password}")

        def savePassword(self, password: str):
            print(f"saving {password}")
   ```
   for example in above code snippet the class `PasswordHasher` is doing two independent
   operations, and the actor that can change its implementation can be security team
   which can change hashing implementation or data team which may change how passwords
   are stored, this doesnt follow single responsiblity principle
   Both functionalities should be seperated
   ```py
    class PasswordHasher:
        def hashPassword(self, password: str):
            print(f"hashing {password}")


    class PasswordStorage:
        def savePassword(self, passwordHash: str):
            print(f"saving {passwordHash}")
   ```


### Open Close:
  open for extension but closed for modification
  ```py
    class HashingType:
        pass


    class PasswordHasher:
        def __init__(self, password: str, hashingType: HashingType):
            self.password = password
            self.hashingType = hashingType

        def hashPassword(self):
            if self.hashingType == "base64":
                # hash password with bas64
                pass
            elif self.hashingType == "sha256":
                # hash password with sha256
                pass
            elif self.hashingType == "md5":
                # hash password with md5
                pass
  ```
  in above code snippet, if we need to add one more hashing type, we need to modify the
  `PasswordHasher` class which voilates the Open Close principle.
  We should make the `HashingType` class more extensible
  ```py
    class IHashingType(metaclass=ABCMeta):
        @abstractmethod
        def hashPassword(self, password: str):
            pass


    class Base64Hashing(IHashingType):
        def hashPassword(self, password: str):
            # hash password with bas64
            pass


    class Md5Hashing(IHashingType):
        def hashPassword(self, password: str):
            # hash password with md5
            pass


    class SHA256Hashing(IHashingType):
        def hashPassword(self, password: str):
            # hash password with sha256
            pass


    class PasswordHasher:
        def __init__(self, password: str, hashingType: IHashingType):
            self.password = password
            self.hashingType = hashingType

        def hashPassword(self):
            self.hashingType.hashPassword(self.password)
  ```
  This way we just need to add another class for different hashing type


### Liskov Substution:
  if their is f(x) for some object x of class A
  then their should be f(y) for some object y of class B if B inherits A
  if class CitrusFruit inherit class Fruit
  then eat(fruit) should support both, orange of CitrusFruit and banana of Fruit
  function should take argument of both base class and derived class and should not break

```py
    class Fruit:
        def __init__(self, name: str):
            self.name = name


    class CitrusFruit(Fruit):
        pass


    def eat(fruit):
        if isinstance(fruit, CitrusFruit):
            print(f"Eating citrus fruit: {fruit.name}")
        elif isinstance(fruit, Fruit):
            print(f"Eating fruit: {fruit.name}")


    banana = Fruit("banana")
    orange = CitrusFruit("orange")

    eat(banana)
    eat(orange)
```
  here the behaviour of `eat()` changes with the type of object it is passed which doest
  follow liskov substitution principle
  ```py
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
  ```
  Now `eat()` behaves same for `Fruit` or its subclass `CitrusFruit`


### Interface Segregation:
  design multiple smaller interfaces
  ```py
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
  ```


### Dependency Inversion:
  high level module should not depend on low level module
  both should depend on abstraction
  abstraction should not depend on implementation
  implementation shouldnt depend on abstraction
  ex: store class has a fn makePayment which makes payment
  instead of initializing a class StripePayment in it
  make a interface HandlePayment, StripePayment and Paypalpayment both extends it
  not pass any object of HandlePayment interface in makePayment fn
```py
    class StripePayment:
        def makePayment(self):
            pass


    class Store:
        def makeStripePayment(self):
            stripePayment = StripePayment()
            stripePayment.makePayment()
```
  the fn `makeStripePayment()` initializes the object of `StripePayment` in its implementation
  suppose we need to test it using Mock payment api, then we it would be hard for us as we need to change the implementation of fn just to test.
  so instead of initializing payment object and depending on its concreat
  implementation we should depend on an interface instead (which will be implemented by
  StripePayment class) and take that as an argument
  ```py
    class IPayment:
        def makePayment(self):
            pass


    class StripePayment(IPayment):
        def makePayment(self):
            print("making payment using stripe")


    class Store:
        def makePayment(self, paymentObj: IPayment):
            paymentObj.makePayment()


    store = Store()
    stripePayment = StripePayment()
    store.makePayment(stripePayment)
  ```

