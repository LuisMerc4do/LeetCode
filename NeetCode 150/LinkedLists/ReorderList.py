def reorderList(head):
    if not head or not head.next:
        return head

    #Find middle node with slow fast pointers
    slow = head
    fast = head
    # at the end of the iteration slow should be at the middle, if even middle + 1
    while fast and fast.next:
        fast = fast.next.next # increment fast by 2
        slow = slow.next # increment slow by 1
    # Now we have our list in half, we need to reverse the right half
    prev = None
    curr = slow
    while curr:
        # we take the next number after middle node
        next_ = curr.next
        # we change the direction of the next node to the opposite way
        curr.next = prev
        prev = curr
        curr = next_
    
        # Now we need to merge the first and reversed second half
    first = head
    second = prev
    # so prev here is the head node in the new list [5 => 4 => 3 => None], first half is [1 => 2]
    while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
    return head

"""
first = head, second = prev: After reversing the second half, the first pointer is at the head of the original list, and the second pointer is at the head of the reversed second half.

while second.next: We merge the two halves of the list. In each iteration, we alternately connect nodes from the first half (first) and the second half (second).

first.next = second: The first node points to the first node from the reversed second half (5).

first = first.next: Move the first pointer to the node after the head, which now points to 5.

second.next = first: The second 
node (5) now points to the next node in the first half (2).

second = second.next: Move the second pointer to the next node, which points to 2.

This process continues until we merge both halves."""
