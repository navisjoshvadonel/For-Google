class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    dummy = ListNode(0)   # dummy starting node
    curr = dummy          # pointer to build result

    while list1 and list2:
        if list1.val <= list2.val:
            curr.next = list1       # attach list1's node
            list1 = list1.next      # move list1 forward
        else:
            curr.next = list2       # attach list2's node
            list2 = list2.next      # move list2 forward
        curr = curr.next            # move result pointer forward

    # attach remaining nodes
    if list1:
        curr.next = list1
    if list2:
        curr.next = list2

    return dummy.next   # skip dummy, return actual head

# Build list1: 1 → 2 → 4
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

# Build list2: 1 → 3 → 4
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

# Merge
result = mergeTwoLists(list1, list2)

# Print
curr = result
while curr:
    print(curr.val, end=" → ")
    curr = curr.next
# Output: 1 → 1 → 2 → 3 → 4 → 4