# Objects:
# Cache has Storage and EvictionPolicy

# Behaviour
# cache can get, put key,value
# Storage can get,put,delete key, value
# Cache will tell EvictionPolicy that key is accessed/added
# EvictionPolicy can give key to evict

from abc import abstractmethod, ABCMeta
from dll import DoublyLinkedList, Node


class EvictionPolicy(metaclass=ABCMeta):
    @abstractmethod
    def evictKey(self):
        pass

    @abstractmethod
    def accessedKey(self, key: str):
        pass


class Storage(metaclass=ABCMeta):
    @abstractmethod
    def get(self, key: str):
        pass

    @abstractmethod
    def put(self, key: str, val: str):
        pass

    @abstractmethod
    def delete(self, key: str):
        pass


class LRUEvictionPolicy(EvictionPolicy):
    def __init__(self):
        self.dll = DoublyLinkedList()
        self.map: dict[str, Node] = {}

    def evictKey(self):
        toEvict = self.dll.tail
        self.dll.removeBack()
        return toEvict

    def accessedKey(self, key: str):
        if key not in self.map:
            node = Node(key)
            self.map[key] = node
        else:
            self.dll.detach(self.map[key])
        self.dll.addFront(self.map[key])
        self.dll.trav()


class DictStorage(Storage):
    def __init__(self, size):
        self.size = size
        self.store = {}

    def get(self, key: str):
        if key in self.store:
            return self.store[key]
        return None

    def put(self, key: str, value: str) -> bool:
        if len(self.store) >= self.size and key not in self.store:
            return False
        self.store[key] = value
        return True

    def delete(self, key: str) -> bool:
        if key in self.store:
            self.store.pop(key)
            return True
        return False


class Cache:
    def __init__(self, storage, evictionPolicy):
        self.storage = storage
        self.evictionPolicy = evictionPolicy

    def get(self, key) -> str | None:
        value = self.storage.get(key)
        if value:
            return value
        else:
            return None

    def put(self, key: str, value: str) -> None:
        if not self.storage.put(key, value):
            keyToEvict = self.evictionPolicy.evictKey()
            self.storage.delete(keyToEvict.val)
            print(f"add: {key}, evict :{keyToEvict.val}")
            self.storage.put(key, value)
        self.evictionPolicy.accessedKey(key)


dictStorage = DictStorage(3)
lruEv = LRUEvictionPolicy()
cache = Cache(storage=dictStorage, evictionPolicy=lruEv)
cache.put("a", "dhruv")
cache.put("b", "yash")
cache.put("c", "me")
cache.put("a", "DHRuv")
cache.put("d", "you")
cache.put("e", "lkj")
cache.put("d", "sharma")
print(cache.get("a"))
print(cache.get("b"))
print(cache.get("c"))
print(cache.get("d"))
print(cache.get("e"))
