# https://leetcode.com/problems/peeking-iterator/submissions/1992167852/
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.current_elem = None # dont desync. None or elem


    def peek(self): # should this be safe?
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.current_elem is None: # Haven't peeked yet
            self.current_elem = self.iterator.next()
        return self.current_elem


    def next(self):
        """
        :rtype: int
        """
        if self.current_elem is None:
            elem = self.iterator.next() # could heal here but no need
        else:
            elem = self.current_elem
            self.current_elem = None # moved beyond peek

        return elem


    def hasNext(self):
        """
        :rtype: bool
        """
        if self.current_elem is None:
            return self.iterator.hasNext()
        else:
            return True


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
