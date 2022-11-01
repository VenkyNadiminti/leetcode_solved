# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum=0
        resultNode=ListNode()
        tailnode=resultNode
        while(l1!=None or l2!=None or sum!=0):
            if l1!=None:
                sum+=l1.val
                l1=l1.next
            if l2!=None:
                sum+=l2.val
                l2=l2.next
            newnode=ListNode(sum%10)
            tailnode.next=newnode
            tailnode=newnode
            sum=int(sum//10)
        return resultNode.next
            
