# https://leetcode.com/problems/rotate-list/
# k can be 2*10^9 :D
# 1 2 3 4 5
# -> 4 5 1 2 3
from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class LList:
    def __init__(self):
        self.head = None

    def insert_last(self, new_val):
        new_node = ListNode(new_val)
        if self.head is None:
            self.head = new_node
            return self.head

        tail = self.head
        while tail.next is not None:
            tail = tail.next
        tail.next = new_node
        return self.head

    def show(self):
        traverse = self.head
        while traverse is not None:
            print(traverse.val, end = ' ')
            traverse = traverse.next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        first = head
        list_len = 0
        temp = head
        # Handle if k is 2*10^9
        while temp is not None:
            temp = temp.next
            list_len += 1
        lim = k - (k // list_len) * list_len
        for i in range(lim):
            prev = first
            last = first.next
            while last.next is not None:
                prev = prev.next
                last = last.next
            last.next = first
            first = last
            prev.next = None
            last = prev
        return first

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    k = 2
    sol = Solution()
    llist = ListNode()
    temp = llist
    for i in arr:
        new_node = ListNode(i)
        temp.next = new_node
        temp = temp.next
    llist = llist.next
    ans = sol.rotateRight(llist, k)
    while ans is not None:
        print(ans.val, end=' ')
        ans = ans.next