

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        LN = ListNode()
        L = LN
        while (l1 or l2):
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            div = (a + b + L.val) % 10
            jin = (a + b + L.val) //10
            L.val = div
            # 两个链表都向后移
            if l1 : l1 = l1.next
            if l2 : l2 = l2.next

            # 判断是否需要继续创建新的节点
            if l1 or l2 or jin > 0:
                L.next = ListNode(jin)
                L = L.next
        return LN