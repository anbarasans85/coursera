# python3

import sys, threading
from collections import deque
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))
                self.t = dict()
                for i in range(self.n):
                    if self.parent[i] == -1:
                        self.tr = i
                    if self.parent[i] in self.t:
                        temp = self.t[self.parent[i]]
                        temp.append(i)
                        self.t[self.parent[i]] = temp
                    else:
                        self.t[self.parent[i]] = [i]

        def compute_height(self):
            tq = deque()
            tq.append(self.tr)
            height = 0
            lenv = 1
            temp_list = list()
            while len(tq) != 0:
                node = tq.popleft()
                temp_list.append(node)
                lenv -= 1
                if lenv == 0:
                    height += 1
                    for e1 in temp_list:
                        if e1 in self.t:
                            for e in self.t[e1]:
                                tq.append(e)
                                lenv += 1
                    temp_list = list()
            return height


def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
