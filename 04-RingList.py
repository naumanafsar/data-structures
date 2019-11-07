class Node:
    def __init__(self, data=None):
        self.val = data
        self.next = None

class Ring:
    def __init__(self):
        self.head = None

def __str__(self):
    ret_str = '[ '
    temp = self.head
    while temp is not None:
        ret_str += str(temp.val) + ', '
        temp = temp.next
        
        if temp == self.head:
            break
    ret_str = ret_str.rstrip(', ')
    ret_str += ' ]'
    return ret_str

Ring.__str__ = __str__


def insert(self, index, val):
    new_node = Node(val)
    last = self._get_last()
    
    if index == 0:
        new_node.next = self.head
        self.head = new_node
        
        if last is None:
            self.head.next = self.head
        else:
            last.next = new_node
            
        return
    
    temp  = self.head
    
    counter = 0
    while temp is not None and counter  < index:
        prev = temp
        temp = temp.next
        counter += 1
        
    prev.next = new_node
    new_node.next = temp
    
Ring.insert = insert

def len(self):
    count = 0
    if self.head is None:
        return count

    temp = self.head

    while temp is not None:
        count += 1
        temp = temp.next
        if temp == self.head:
            break

    return count
Ring.len = len


if __name__ == '__main__': 
    r = Ring()
    # r.insert(1, 1)
    r.insert(0, 1)
    r.insert(0, 2)
    r.insert(1, 3)
    r.insert(7, 5)  # different behavrior since it's a ring! 
    print(r)
