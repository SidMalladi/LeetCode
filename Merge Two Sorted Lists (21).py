class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        s1 = []
        s2 = []
        
        while l1:
            s1 += [l1.val]
            l1 = l1.next
        
        while l2:
            s2 += [l2.val]
            l2 = l2.next
        
        s = sorted(s1+s2)  #merge and sort the combined list
        
        point = head = ListNode(0)
        for k in s:
            point.next = ListNode(k)
            point = point.next
        return head.next