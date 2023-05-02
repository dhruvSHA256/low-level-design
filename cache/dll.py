import gc


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addFront(self, node):
        node.next = self.head
        if self.head:
            self.head.prev = node
            self.head = node
            node.prev = None
        else:
            self.head = node
            self.tail = node
            node.prev = None

    def addBack(self, node):
        node.prev = self.tail
        if self.tail:
            self.tail.next = node
            node.next = None
            self.tail = node
        else:
            self.head = node
            self.tail = node
            node.next = None

    def removeFront(self):
        if not self.head:
            return
        temp = self.head
        temp.next.prev = None
        self.head = temp.next
        temp.next = None
        gc.collect()
        return temp.val

    def removeBack(self):
        if not self.tail:
            return
        temp = self.tail
        temp.prev.next = None
        self.tail = temp.prev
        temp.prev = None
        gc.collect()
        return temp.val

    def trav(self):
        node = self.head
        while node:
            print(f"{node.val} ", end="")
            node = node.next
        print("")

    def detach(self, node):
        if node is self.head:
            self.head = node.next
            self.head.prev = None
            return
        if node is self.tail:
            self.tail = node.prev
            self.tail.next = None
            return
        node.prev.next = node.next
        node.next.prev = node.prev


# dll = DoublyLinkedList()
# d = Node(9)
# dll.addFront(Node(10))
# dll.addFront(d)
# dll.addFront(Node(8))
# dll.addBack(Node(20))
# dll.addBack(Node(30))
# dll.addFront(Node(7))
# dll.addBack(Node(40))
# dll.addFront(Node(6))
# dll.removeBack()
# dll.removeFront()
# dll.removeFront()
# dll.removeFront()
# dll.trav()
