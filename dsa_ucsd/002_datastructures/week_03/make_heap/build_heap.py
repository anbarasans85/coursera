# python3
import math

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def GenerateSwaps(self):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    for i in range(len(self._data)):
      for j in range(i + 1, len(self._data)):
        if self._data[i] > self._data[j]:
          self._swaps.append((i, j))
          self._data[i], self._data[j] = self._data[j], self._data[i]

  def parent(self, i):
    return math.floor((i -1)/2)
    
  def left(self, i):
    return (2*i) + 1

  def right(self, i):
    return (2*i) + 2

  def sift_down(self, i):
    maxindex = i
    l = self.left(i)
    if l < len(self._data) and self._data[l] < self._data[maxindex]:
      maxindex = l
    r = self.right(i)
    if r < len(self._data) and self._data[r] < self._data[maxindex]:
      maxindex = r
    if i != maxindex:
      self._swaps.append((i, maxindex))
      self._data[i], self._data[maxindex] = self._data[maxindex], self._data[i]
      self.sift_down(maxindex)

  def build_heap(self):
    for i in (range(math.floor(len(self._data)/2), -1, -1)):
      self.sift_down(i)

  def Solve(self):
    self.ReadData()
    #self.GenerateSwaps()
    self.build_heap()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
