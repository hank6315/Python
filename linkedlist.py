class Node:
    def __init__(self , data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printdata(self):
        cur_node = self.head

        while cur_node :
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        rear_node = self.head
        while rear_node.next :
            rear_node = rear_node.next
        
        rear_node.next = new_node


    def pre_append(self , data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return 

        new_node.next = self.head
        self.head = new_node


    def insert_after_node(self , pre_node, data):
        if not pre_node:
            print('Pre node is not in the list')
            return

        new_node = Node(data)

        new_node.next = pre_node.next
        pre_node.next = new_node    


llist = LinkedList()
llist.append(5)
llist.append(6)
llist.pre_append(2)
llist.insert_after_node(llist.head.next, 4)
llist.printdata()


