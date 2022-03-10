# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 用小顶堆存储 链表中的值，及第几个链表， 每次都从小顶堆中取值，然后再往小顶堆加值（取出的值属于哪个链表，就把这个链表的下个值再存入，直到本次链表遍历完成）
class Solution:
    def mergeKLists(self, lists):
        import heapq
        dumpy = ListNode(0)
        p = dumpy
        head = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(head, (lists[i].val, i))
                lists[i] = lists[i].next
        print(heapq)

        while head:
            val, idx = heapq.heappop(head)
            p.next = ListNode(val)
            p = p.next
            if lists[idx]:
                heapq.heappush(head, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return dumpy.next
