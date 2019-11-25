from linkedlist import LinkedList

  
def remove_duplicates(link):
    
    cur = link.head

    while cur and cur.next:
        if cur.next.data == cur.data :
            cur.next = cur.next.next
        else:
            cur = cur.next

    
    



llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("B")
llist.append("C")
llist.append("D")

remove_duplicates(llist)

llist.printdata()