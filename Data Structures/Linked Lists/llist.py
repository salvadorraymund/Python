class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes != None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node != None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return "->".join(nodes)

    def __iter__(self):
        node = self.head
        while node != None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_end(self, node):
        # while node.next != None:
        #     if node.next == None:
        #         node = node.next
        #         node.next = None
        if self.head == None:
            self.head = node
            return
        # this is the first time i saw 'self' being used as object for iteration
        for current_node in self:
            pass
        current_node.next = node

    def length(self):
        if self.head == None:
            print("Error: Linked list is empty!")
            return None
        total = 0
        node = self.head
        while node.next != None:
            node = node.next
            total += 1
        return total

    def set(self, index, data):
        if index >= self.length() or index < 0:
            print("Error: Index out of range!")
            return None
        current_index = 0
        node = self.head
        while node.next != None:
            if current_index == index:
                node.next = data
                node = node.next
            current_index += 1

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty!")
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

    # Select a target node and insert a new node before it.
    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty!")
        if self.head.data == target_node_data:
            return self.add_first(new_node)
        prior_node = self.head
        for node in self:
            if node.data == target_node_data:
                prior_node.next = new_node
                new_node.next = node
                return
            prior_node = node
        raise Exception("Node with data '%s' not found" % target_node_data)

    # Selct a node to be removed.
    def remove(self, target_node_data):
        if self.head is None:
            raise Exception("The linked list is empty!")
        if self.head.data == target_node_data:
            self.head = self.head.next
            return
        prior_node = self.head
        for node in self:
            if node.data == target_node_data:
                prior_node.next = node.next
                return
            prior_node = node
        raise Exception("Node with data '%s' not found" % target_node_data)

    # Retrieve the data of a node
    def get(self, index):
        if index > self.length() or index < 0:
            raise Exception("Index is out of range!")
        if self.head is None:
            raise Exception("Linked list is empty")
        current_node = self.head
        current_index = 0
        for node in self:
            current_node = node
            if current_index == index:
                return current_node.data
            current_index += 1

    # Select an index of a node and replace its data with a new one.
    def set_data(self, index, new_data):
        if index > self.length() or index < 0:
            raise Exception("Index is out of range!")
        if self.head is None:
            raise Exception("Linked list is empty!")
        current_node = self.head
        current_index = 0
        for node in self:
            current_node = node
            if current_index == index:
                current_node.data = new_data
            current_index += 1

    # Reverse the order of elements in the list.
    def reverse(self):
        prev = None
        current_node = self.head
        while current_node != None:
            nxt = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = nxt
        self.head = prev


llist = LinkedList(['a', 'b', 'c', 'd', 'e'])
# print(llist)
# first_node = Node('a')
# llist.head = first_node
# print(llist)

# second_node = Node('b')
# third_node = Node('c')
# first_node.next = second_node
# second_node.next = third_node
# print(llist)

llist.add_first(Node('xyz'))


llist.add_end(Node('123'))
llist.add_after('a', Node("abakada"))
print(llist)

llist.add_before('xyz', Node('avc'))
print(llist)

llist.add_before('c', Node('chapypabra'))
print(llist)

llist.remove('avc')
print(llist)

print(llist.get(1))

llist.set_data(1, "apple")
print(llist)

llist.reverse()
print(llist)

llist.reverse()
print(llist)
