class Node:
    def __init__(self, data=None):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

def push(self, val):
    """
    Push the value to end of list:
    - Case 1: If list is empty, it create a new node and push value there
    - Case 2: Loop through the end and push value there

    """
    new_node = Node(val)
    
    # Case 1

    if self.head is None:
        self.head = new_node
        return
    
    # Case 2
    last = self.head
    while last.next is not None:
        last = last.next
    last.next = new_node

LinkedList.push = push

def pop(self):

    """
    Pop the last value from the list
    - Case 1: If List is empty, it raise an exception
    - Case 2: If List has only one value, pop the value and set self.head to None
    - Case 3: Otherwise loop through the end and pop the value
    """
    
    # Case 1
    if self.head is None:
        raise Exception ("Cannot pop. List is empty")
    
    # Case 2
    if self.head.next is None:
        val = self.head.val
        self.head = None
        return val
    
    # Case 3
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

def len(self):

    """
    Simply returns the length of Linked List
    """
    count = 0
    
    if self.head is None:
        return count
    
    temp = self.head
    while temp is not None:
        temp = temp.next
        count += 1
    return count

LinkedList.len = len

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
    if temp is not None:
        prev.next = temp.next
        return
    else:
        prev.next = temp
        return
LinkedList.remove = remove

def reverse_list(self):
    
    if self.head is None: return
    if self.head.next is None: return
    
    new_head = self._get_last()
    processing = new_head
    
    for i in range(self.len() -1):
        temp = self.head
        while temp.next  != processing:
            temp = temp.next
        processing.next = temp
        processing = processing.next
    
    self.head.next = None
    self.head = new_head
    
LinkedList.reverse_list = reverse_list


if __name__ == '__main__': 
    l = LinkedList() 
    l.push(1) 
    l.push(2)
    l.push(3)

    print(l)

    l.reverse_list() 
    print(l)

