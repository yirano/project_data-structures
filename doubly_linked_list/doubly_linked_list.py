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
        self.length += 1
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        print(">>>>>>>>>>>>>>> ROUND: ", self.rounds)
        print('Add to head: ', self.head.value)
        print('>> Head value? ', self.head.value)
        print('>> Tail value? ', self.tail.value)

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        if not self.head:
            self.length = 0
            return None
        if self.head.next is None:
            self.length = 0
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        self.length -= 0
        head_value = self.head.value
        self.head = self.head.next
        return head_value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        self.length += 1
        new_node = ListNode(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail = new_node
            self.head.next = new_node.prev

        print(">>>>>>>>>>>>>>> ROUND: ", self.rounds)
        print('Add to tail: ', self.tail.value)
        print('>> Head value? ', self.head.value)
        print('>> Head next value? ', self.head.next.value)
        print('>> Tail prev value? ', self.tail.prev.value)
        print('>> New tail value? ', self.tail.value)
        # print('>> Head next value? ', self.head.next.value)
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        if not self.tail:
            self.length = 0
            return None
        if self.tail.prev is None:
            self.length = 0
            tail_value = self.tail.value
            self.head = None
            self.tail = None
            return tail_value
        self.length -= 0
        tail_value = self.tail.value
        self.tail = self.tail.prev
        return tail_value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        if self.head == None:
            self.head = node
        else:
            node.next = self.head  # node is going to point to the current self.head
            self.head = node  # the new self.head is the node

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def count(self):
        self.rounds += 1
        return self.rounds

    def move_to_end(self, node):
        if self.length == 2:
            node.prev = self.tail
            self.tail = node
            self.head = node.prev
        else:
            # node.prev = self.tail
            # self.tail = node
            pass
        print(">>>>>>>>>>>>>>> ROUND: ", self.rounds)
        print('Move to end: ', self.tail.value)
        print('>> Tail value? ', self.tail.value)
        # print('>> Tail Prev value? ', self.tail.prev.value)
        print('>> Head value? ', self.head.value)
        print('>> NODE VALUE? ', node.value)
        print('>> Length? ', self.length)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        return f'HI'

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        pass
