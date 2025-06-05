"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        def flattenDFS(prev, curr):
            if not curr:
                return prev
            
            curr.prev = prev
            prev.next = curr

            tempNext = curr.next  
            tail = flattenDFS(curr, curr.child) 
            curr.child = None  
            return flattenDFS(tail, tempNext) 

        dummy = Node(0)
        flattenDFS(dummy, head)
        dummy.next.prev = None 
        return dummy.next
        