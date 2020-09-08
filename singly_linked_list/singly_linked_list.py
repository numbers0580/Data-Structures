class Node:
    def __init__(self, value=None):
        self.value = value
        # ALWAYS set next to None. Thus, "next" doesn't have to be in the parameters above
        self.next = None

    def getvalue(self):
        return self.value

    def getnextnode(self):
        return self.next

    def setnode(self, anode):
        self.next = anode

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_tail(self, val):
        newnode = Node(val)
        if self.head is None:
            # No need to check if tail == None if we already know that head == None. We're setting the first node here
            self.head = newnode
            self.tail = newnode
        else:
            # There is at least one node in the LinkedList, just set the tail
            self.tail.setnode(newnode)
            self.tail = newnode

    def remove_head(self):
        if self.head is None:
            # Effectively, if the LinkedList is empty
            return None
        # Storing the current value of the head BEFORE we make modifications
        val = self.head.getvalue()
        if self.head is self.tail:
            # Effectively, if wee only have exactly one node in the LinkedList
            self.head = None
            self.tail = None
        else:
            # There's a head and a different tail, make head refer to the next node instead
            self.head = self.head.getnextnode()
        return val

    def remove_tail(self):
        if self.head is None:
            # Effectively, if the LinkedList is empty
            return None
        # Storing the current value of the tail BEFORE we make modifications
        val = self.tail.getvalue()
        if self.head == self.tail:
            # Effectively, if wee only have exactly one node in the LinkedList
            self.head = None
            self.tail = None
        else:
            # There's a head and a tail. Start from the head...
            current = self.head
            # Search through LinkedList until you find the node that is referring to the tail as the next node...
            while current.getnextnode() != self.tail:
                current = current.getnextnode()
            # Make that node you found above be the new tail
            self.tail = current
        return val