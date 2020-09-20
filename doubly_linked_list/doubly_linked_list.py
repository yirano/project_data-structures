"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    '''
    Wraps the given value in a ListNode and insert it after this node. Note that this node could already have a next node it is pointing to.
    '''

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    '''
    Wrap the given value in a ListNode and insert it before this node. Note that this nod ecould already have a previous node it is pointing to.
    '''

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    '''
    Rearranges this ListNode's previous and next pointers accordingly, effectively deleting this ListNode.
    '''

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
            # next_node = self.next
            # next_node.prev = self.prev


"""
Our doubly-linked list class. It holds references to
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0
        self.rounds = 1

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        new_node = ListNode(value)
        # if list is currently empty
        if self.head is None and self.tail is None:
            # set the head and tail to equal the new node
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            # the list already has elements in it
            # make new node's next val to curr head
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        if self.head is None:
            return
        else:
            # self.length -= 1
            head_value = self.head.value
            self.delete(self.head)
            return head_value

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        if self.tail is None:
            return
        else:
            # self.length -= 1
            tail_value = self.tail.value
            self.delete(self.tail)
            return tail_value
    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        if self.head == self.tail:
            self.head = node
            self.tail = node
        else:
            old_value = node.value
            self.delete(node)
            new_node = ListNode(old_value)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1

    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        # print('length: ', self.length)
        # print('head: ', self.head.value)
        # print('head next: ', self.head.next.value)
        # print('tail: ', self.tail.value)
        if self.head == self.tail:
            self.head = node
            self.tail = node
        else:
            old_value = node.value
            self.delete(node)
            new_node = ListNode(old_value)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        # print('--------------')
        # print('after head: ', self.head.value)
        # print('after head next: ', self.head.next.value)
        # print('after tail: ', self.tail.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        # the list is empty -> do nothing
        if self.head is None and self.tail is None:
            return
        # the list is only one node
        self.length -= 1
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # the node is the head node
        elif self.head is node:
            self.head = node.next
            self.head.prev = None
            # node.delete()
        # the node is the tail node
        elif self.tail is node:
            self.tail = node.prev
            self.tail.next = None
            # node.delete()
        # the node is just some node in the list
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.next = None
            node.delete()
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        if self.head is None and self.tail is None:
            return
        
        if self.head is self.tail:
            return self.head.value
        else:
            temp = self.head.next
            max_value = temp.value
            
            while(temp):
                print('MAX: ', max_value)
                if(temp.prev.value > temp.value):
                    max_value = temp.prev.value
                else:
                    max_value = temp.value
                temp = temp.next
        return max_value
