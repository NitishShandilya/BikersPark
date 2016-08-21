"""
Node class has the data and a pointer that is used to point to the next Node object.
"""
class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, next_node):
        self.next_node = next_node

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insertFront(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.get_next():
                current = current.get_next()

            current.set_next(new_node)

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        if current == None:
            return "No elements present to search. Please insert elements first."

        found = False
        while current and found == False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()

        if current == None:
            return "Value not found"
        return "Match Found"

    def delete(self, data):
        current = self.head
        if current == None:
            return "No elements present to delete. Please insert elements first."

        found = False
        prev = None
        while current and found == False:
            if current.get_data() == data:
                found = True
            else:
                prev = current
                current = current.get_next()

        if current == None:
            return "Value not found"

        if prev == None:
            self.head = current.get_next()
        else:
            prev.set_next(current.get_next())
        return "Successfully deleted " + str(data)

    def printElements(self):
        current = self.head
        if current == None:
            print "No elements present. Please insert elements."
            return
        while current:
            print current.get_data()
            current = current.get_next()

#Test
list = LinkedList()
list.printElements()
print list.delete(5)
list.append(4)
list.append(5)
list.append(6)
list.append(7)
list.printElements()
print list.delete(7)
list.printElements()
print list.size()