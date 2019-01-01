# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current,last=head,head.next
        while(last):
            current=current.next
            if last.next is not None:
                last=last.next.next
            else:
                last=last.next
        return current
        
        
#------------------------------------------------------------#
#after seeing solution  littlemodification in my solution
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current,last=head,head
        while(last and last.next):
            current=current.next
            last=last.next.next
        return current
