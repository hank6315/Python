from linkedlist import LinkedList

  
def move_tail_to_head(link):
    
    last = link.head
    temp = None
    while last.next:
        temp = last
        last = last.next
    last.next = link.head
    temp.next = None
    link.head = last


     

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

move_tail_to_head(llist)

llist.printdata()