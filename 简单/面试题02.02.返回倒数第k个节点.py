class Solution:
    def kthToLast(self, head,k):
        x = []
        while(head):
            x.append(head.val)
            head = head.next
        return x[len(x)-k]