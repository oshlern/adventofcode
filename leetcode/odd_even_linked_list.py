# https://leetcode.com/problems/odd-even-linked-list/submissions/1992170793/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def display(text: str, head: Optional[ListNode]):
    out = ""
    while head:
        out += str(head.val) + " -> "
        head = head.next
    print(text, out)

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        odd_start = ListNode(head.val, None)
        even_start = ListNode(head.next.val, None)
        starts = [even_start, odd_start]
        ends = [even_start, odd_start]

        head = head.next.next

        i = 3
        while head:
            is_odd = i % 2
            new_node = ListNode(head.val, None)
            ends[is_odd].next = new_node
            ends[is_odd] = new_node
            head = head.next
            # display("evens", starts[0])
            # display("odds", starts[1])
            i += 1
            if i == 10:
                break

        ends[1].next = starts[0]
        return starts[1]
