from linkedlist import LinkedList

  
def reverse_linklist(link):
    pre = None
    cur = link.head

    while cur:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp

    link.head = pre
    



llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

reverse_linklist(llist)

llist.printdata()