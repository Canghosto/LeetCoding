# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#This definetly needs some optimization


class Solution(object):
    def increaseNextByOne(self, data):
        tmp = data.next
        tmp.val += 1
        data.next = tmp
        return data

    def addTwoNumbers(self, l1, l2):
        result = ListNode(l1.val + l2.val)
        count = 0
        if result.val >= 10:
            count = 1
            result.val -= 10
        if l1.next != None and l2.next != None:
            if count > 0:
                l1 = self.increaseNextByOne(l1)
            result.next = self.addTwoNumbers(l1.next, l2.next)
        elif l1.next != None and l2.next == None:
            if count > 0:
                l1 = self.increaseNextByOne(l1)
            result.next = self.addTwoNumbers(l1.next, ListNode(0))
        elif l1.next == None and l2.next != None:
            if count > 0:
                l2 = self.increaseNextByOne(l2)
            result.next = self.addTwoNumbers(ListNode(0), l2.next)
        
        if count > 0 and result.next == None:
            result.next = ListNode(1)
        
        return result