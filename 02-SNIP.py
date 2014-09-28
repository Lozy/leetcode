#!/usr/bin/env python
# -*- coding: utf-8 -*-
# CODE: Swap Nodes in Pairs

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head == None or head.next == None:
            return head
        dummy=ListNode(0)
        dummy.next=head
        
        temp=dummy # temp 从第0个位置 到第2个位置 跳跃 dummy(temp)->A->B->C->D  dummy->B->A(temp)->C->D
        while temp.next and temp.next.next:
            tmp = temp.next.next
            temp.next.next = tmp.next
            tmp.next = temp.next
            temp.next = tmp
            temp = temp.next.next
        
        return dummy.next
