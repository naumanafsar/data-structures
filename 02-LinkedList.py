class Node:
    def __init__(self, data=None):
        self.val = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

def push(self, val):
    new_node = Node(val)
    
    # no node
    if self.head is None:
        self.head = new_node
        return
    
    # otherwise reach the end and insert
    last = self.head
    while last.next is not None:
        last = last.next
    last.next = new_node
LinkedList.push = push

def pop(self):
    if self.head is None:
        raise Exception ("Cannot pop. No value")
    
    if self.head.next is None:
        val = self.head.val
        self.head = None
        return val
    
    temp = self.head
    while temp.next is not None:
        prev = temp
        temp = temp.next
    
    val = temp.val
    prev.next = None
    return val

LinkedList.pop = pop


def __str__(self):
    ret_str = ' [ '
    temp = self.head
    while temp is not None:
        ret_str += str(temp.val) + ' ,  '
        temp = temp.next
    ret_str = ret_str.rstrip(' ,  ')
    ret_str += ' ]'
    return ret_str
LinkedList.__str__ = __str__

def insert(self, index, val):
    new_node = Node(val)
    
    if index == 0:
        new_node.next = self.head
        self.head = new_node
        return
    
    temp = self.head
    
    counter = 0
    while temp is not None and counter < index:
        prev = temp
        temp = temp.next
        counter += 1
    
    prev.next = new_node
    new_node.next = temp

LinkedList.insert = insert

def remove(self, val):
    
    temp = self.head
    
    if temp is not None:
        if temp.val == val:
            self.head = temp.next
            temp = None
            return
    
    
    while temp is not None:
        if temp.val == val:
            break
        
        prev = temp
        temp = temp.next
    
    if temp is None:
        return
    
    prev.next = temp.next

LinkedList.remove = remove


def len(self):
    count = 0
    
    if self.head is None:
        return count
    
    temp = self.head
    while temp is not None:
        temp = temp.next
        count += 1
    return count

LinkedList.len = len


def get(self, index):
    temp = self.head
    count = 0

    if index > self.len() -1:
        raise IndexError("Index out of bound")
    
    while temp is not None:
        if count == index:
            return temp.val
        count += 1
        temp = temp.next

LinkedList.get = get




if __name__ == "__main__": 
    l = LinkedList() 
    l.push(5) 
    l.push(6) 

    print(l)

    print(l.len())

    l.pop() 
    print(l.len())

    print(l.get(0))
    l.get(2) # Should say "IndexError: Index out of bound"

