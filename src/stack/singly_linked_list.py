# from multiprocessing.process import current_process


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None  # stores a node that corresponds to our first node in the list
        self.tail = None  # stores a node that is at the end of the list

    def add_to_head(self, value):
        # create a node to add
        new_node = Node(value)

        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # new_node should point to current head
            new_node.next_node = self.head
            # move head to new node
            self.head = new_node

    def add_to_tail(self, value):
        # create a node to add
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.tail = new_node
            self.head = new_node
        else:
            # point the node at the curr tail to the new node
            self.tail.next_node = new_node
            self.tail = new_node

    # remove the head and return its value
    def remove_head(self):
        # if list is empty do nothing
        if not self.head:
            return None
        # if list only has one element, set head and tail to None
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None

            return head_value
        # otherwise we have more elements in the list
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value

    def len(self):
        temp = self.head
        count = 0
        while(temp):
            count += 1
            temp = temp.next_node
        return count

    def contains(self, value):
        if self.head is None:
            return False

        # loop through each node, until we see the value, or we cannot go further
        current_node = self.head

        while current_node is not None:
            # check if this is the node  we are looking for
            if current_node.value == value:
                return True

            # otherwise, go to the next node
            current_node = current_node.next_node
        return False


# linked_list = LinkedList()

# linked_list.add_to_head(0)
# linked_list.add_to_tail(1)

# print(f'does our LL contain 0? {linked_list.contains(0)}')
# print(f'does our LL contain 1? {linked_list.contains(1)}')

# linked_list.add_to_head(2)
# print(f'the start of the list is {linked_list.head.value}')
