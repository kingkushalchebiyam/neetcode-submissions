# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if not head or not head.next: 
            return
        
        nodes = []
        curr = head
        while curr: 
            nodes.append(curr)
            curr = curr.next
        
        j = 0
        i = len(nodes)-1

        while j < i: 
            nodes[j].next = nodes[i]
            j+=1 

            nodes[i].next = nodes[j]
            i-=1
        
        nodes[j].next = None
        
       
          


        

            


        
        

        

        





        