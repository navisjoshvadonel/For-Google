class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next   # save next before breaking arrow
        curr.next = prev        # flip the arrow
        prev = curr             # move prev forward
        curr = next_node        # move curr forward

    return prev   # prev is now the new head

# Build list: 1 → 2 → 3 → 4 → 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Reverse it
new_head = reverseList(head)

# Print result
curr = new_head
while curr:
    print(curr.val, end=" → ")
    curr = curr.next
# Output: 5 → 4 → 3 → 2 → 1 →