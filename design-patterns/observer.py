# observer: Behavioural pattern

class Observer:
    def __init__(self, name):
        self.name = name

    def update(self, msg, observable):
        print(f"Update by {observable.name}: {msg} for {self.name}")

class Observable:
    def __init__(self, name):
        self.name = name
        self.__subscribers = []
        self.__articles = []

    def add(self, article):
        self.__articles.append(article)
        self.notify(article)

    def subscribe(self, subscriber):
        self.__subscribers.append(subscriber)

    def unsubscribe(self, subscribe):
        self.__subscribers.remove(subscribe)

    def notify(self, article):
        for sub in self.__subscribers:
            sub.update(article, self)

if __name__ == '__main__':
    observable = Observable('Cart')
    observer1 = Observer('user1')
    observer2 = Observer('user2')
    observable.subscribe(observer1)
    observable.subscribe(observer2)
    observable.add('iphone')
    observable.unsubscribe(observer2)
    observable.add('iwatch')
