
class ListNode(object):
    def __init__(self, val=0, next=None):
      self.val = val
      self.next = next
      
class Solution:
    def deleteDuplicates(self, head):
        if not head: # if list is empty
            return None

        curr = head #points to front of linked list

        while curr.next:# while we aren't at end of list
            if curr.val == curr.next.val: # if nxt node has same value
                curr.next = curr.next.next  # skip duplicate value
            else:  # not a duplicate
                curr = curr.next

        return head # return front of linked list