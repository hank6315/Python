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

    def delete(self, data):

        cur_node = self.head

        if cur_node and cur_node.data == data:
            self.head = cur_node.next
            cur_node = None
            return 
        
        pre = None
        while cur_node and cur_node.data != data:
            pre = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        pre.next = cur_node.next
        cur_node = None 

    def count_length(self):
        count = 0

        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next

        return count


    
    def reverse_linklist(self):
        pre = None
        cur = self.head

        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        self.head = pre
       
        


