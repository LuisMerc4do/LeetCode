# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(head):
        """
        :type head: ListNode
        :rtype: bool
        """
        newList = []
        current = head
        while current:
            newList.append(current)
            current = current.next
        left = 0
        rigth = len(newList) - 1
        while left < rigth:
            if newList[left] == newList[rigth]:
                left += 1
                rigth -= 1
            else:
                return False
        return True
    isPalindrome([1,2,2,1])