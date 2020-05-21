"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.next:
            self.next.prev = self.prev

        if self.prev:
            self.prev.next = self.next

    def __str__(self):
        output = ''
        current_node = self
        while current_node:
            if current_node.prev:
                output += " => "
            output += str(current_node.value)
            current_node = current_node.next
        return output

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        self.length += 1
        new_node = ListNode(value)
        if self.head is None and self.tail is None:
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head

        self.head = new_node


    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        removed_node = self.head
        if len(self) == 0:
            return
        if len(self) == 1:
            self.head = None
            self.tail = None
        else:
            self.head.next.prev = None
            self.head = self.head.next

        self.length -= 1
        return removed_node.value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        self.length += 1
        new_node = ListNode(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        self.length -= 1
        removed_node = self.tail
        if self.head is None and self.tail is None:
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail.prev.next = None
        return removed_node.value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if len(self) == 0:
            return
        elif len(self) == 1:
            return
        else:
            self.delete(node)
            self.add_to_head(node.value)


    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if self.head is None and self.tail is None:
            return
        elif self.head == self.tail:
            return
        else:
            self.delete(node)
            self.add_to_tail(node.value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if len(self) == 0:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
        elif self.head.value == node.value:
            self.remove_from_head()
        elif self.tail.value == node.value:
            self.remove_from_tail()
        else:
            self.length -= 1
            current_node = self.head
            while current_node:
                if current_node.value == node.value:
                    if current_node.prev:
                        current_node.prev.next = current_node.next
                    if current_node.next:
                        current_node.next.prev = current_node.prev
                current_node = current_node.next

        
    """Returns the highest value currently in the list"""
    def get_max(self):
        current_node = self.head
        max_value = current_node.value
        while current_node:
            if current_node.value > max_value:
                max_value = current_node.value
            current_node = current_node.next
        return max_value
