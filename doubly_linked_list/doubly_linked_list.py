"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        if self.length > 0:
            current = self.head
            self.head = ListNode(value, None, current)
            current.prev = self.head
        else:
            self.head = ListNode(value)
            self.tail = ListNode(value) # I had to add this line in to get test_list_remove_from_head to pass
        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None:
            return None
        else:
            val = self.head.value

            if self.length <= 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None

            self.length -= 1
            return val
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        if self.tail:
            current = self.tail
            self.tail = ListNode(value, current)
            current.next = self.tail
        else:
            self.head = ListNode(value)
            self.tail = ListNode(value)
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.head is None:
            return None
        else:
            val = self.tail.value

            if self.length <= 1:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None

            self.length -= 1
            return val
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.head:
            if self.head != node:
                preceding = node.prev
                preceding.next = node.next
                if self.tail != node:
                    node.next.prev = preceding
                else:
                    self.tail = preceding
                front = self.head
                self.head = ListNode(node.value, None, front)
                front.prev = self.head
        else:
            self.head = node
            self.tail = node
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.head:
            if self.tail != node:
                latter = node.next
                latter.prev = node.prev
                if self.head != node:
                    node.prev.next = latter
                else:
                    self.head = latter
                back = self.tail
                self.tail = ListNode(node.value, back)
                back.next = self.tail
        else:
            self.head = node
            self.tail = node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # if self.head is None:
        #     return None
        # if node.next:
        #     node.next.prev = node.prev
        # else:
        #     # New tail?
        #     pass

        
        # if node.prev:
        #     node.prev.next = node.next
        # else:
        #     # New head?
        #     pass

        
        # if self.head is node:
        #     self.head = node.next

        # if self.tail is node:
        #     self.tail = node.prev
        # self.length -= 1
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node is self.head:
            self.head = node.next
        if node is self.tail:
                self.tail = node.prev
        self.length -= 1
        

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.head is None:
            return None
        else:
            current = self.head
            val = self.head.value

            while current:
                if current.value > val:
                    val = current.value
                current = current.next

            return val