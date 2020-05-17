# Implementation of Priority Queue
class PriorityQueue:
    def __init__(self, s=63):
        self.pq = [None]*s
        self.size = 0

    def parent(self, i):
        return (i-1)//2

    def add(self, x):
        if len(self.pq) == self.size:
            print("Priority Queue is full!")
        else:
            self.pq[self.size] = x
            self.percolate_up(self.size)
            self.size += 1

    def percolate_up(self, i):
        x = self.pq[i]
        while i > 0 and x < self.pq[self.parent(i)]:
            self.pq[i] = self.pq[self.parent(i)]
            i = self.parent(i)
        self.pq[i] = x

    def remove(self):
        first = self.pq[0]
        self.size -= 1
        self.pq[0] = self.pq[self.size]
        self.percolate_down(0)
        return first

    def percolate_down(self, i):
        x = self.pq[i]
        c = (2 * i) + 1
        while c <= self.size-1:
            if c < self.size-1 and self.pq[c] > self.pq[c+1]:
                c += 1

            if x <= self.pq[c]:
                break

            self.pq[i] = self.pq[c]
            i = c
            c = (2*i) + 1
        self.pq[i] = x

    def peek(self):
        return self.pq[0]


