import sys

class MinHeap:
    def __init__(self):
        self.queue = []

    def insert(self, x):
        self.queue.append(x)
        last_idx = len(self.queue) - 1

        while last_idx >= 0:
            parent_idx = self.parent(last_idx)
            if 0 <= parent_idx and self.queue[parent_idx] > self.queue[last_idx]:
                self.swap(last_idx, parent_idx)
                last_idx = parent_idx 
            else:
                break

    def minHeapify(self,i):
        left_idx = self.left_child(i)
        right_idx = self.right_child(i)
        min_idx = i

        if left_idx <= len(self.queue)-1 and self.queue[min_idx] >= self.queue[left_idx]:
            min_idx = left_idx
        if right_idx <= len(self.queue)-1 and self.queue[min_idx] >= self.queue[right_idx]:
            min_idx = right_idx
        
        if min_idx != i:
            self.swap(i, min_idx)
            self.minHeapify(min_idx)

    def parent(self, idx):
        return (idx-1)//2
    
    def left_child(self,idx):
        return 2*(idx+1) - 1
    
    def right_child(self,idx):
        return 2*(idx+1)

    def swap(self, i,j):
        self.queue[i], self.queue[j] = self.queue[j], self.queue[i]

    def delete(self):
        last_idx = len(self.queue) - 1
        if last_idx < 0:
            print(0)
            return
        self.swap(0, last_idx)
        minv = self.queue.pop()
        self.minHeapify(0)
        print(minv)
        return minv 


n = int(sys.stdin.readline().rstrip())

heap = MinHeap()

for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x > 0:
        heap.insert(x)
    elif x == 0:
        heap.delete()
