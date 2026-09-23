# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        nodes = []
        cur = head
        while cur: 
            nodes.append(cur)
            cur = cur.next
        
        length = len(nodes)
        removedNode = length - n

        if removedNode == 0: 
            return head.next
        
        prev_node = nodes[removedNode-1]

        if removedNode + 1 < length: 
            next_node = nodes[removedNode+1] 
        else: 
            next_node = None

        prev_node.next = next_node

        return head

        