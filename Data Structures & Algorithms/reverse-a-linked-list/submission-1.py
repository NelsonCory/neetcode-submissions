# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #iterate to  end of list, then move nodes from head to  until head = original tail
        # ABCD
        # DCBA

        if not head:
            return None
        
        originalHead = head
        originalTail = self.returnTail(originalHead)
        curr = originalHead
        while(curr != originalTail):
            #self.printList(curr)
            nextNode = self.insertNode(curr,originalTail)
            curr = nextNode
        #self.printList(curr)
        return curr

    def returnTail(self,head):
        curr = head
        while curr.next:
            curr = curr.next
        return curr

    def insertNode(self,node,tail):
        temp = node.next
        node.next = tail.next
        tail.next = node
        return temp

    def printList(self,head):
        curr = head
        nodes = []
        print(curr)
        while curr.next:
            nodes.append(curr.val)
            curr = curr.next
        nodes.append(curr.val)
        print(nodes)