#specialized min heap for dijkstra prime algorithm
#we will never remove an element, so the array will only grow
#therefore, we need not track the empty index or array size
#and we can use dynamic resizing of the array
class minHeap():
    def __init__(self):
        self.arr  = []
    def parentIndex(self, childIndex):
        return (childIndex - 1) // 2
    def leftChildIndex(self, parentIndex):
        return 2 * parentIndex + 1
    def rightChildIndex(self, parentIndex):
        return 2 * parentIndex + 2
    def inRange(self, index):
        return index >= 0 and index < len(self.arr)
    def insert(self, pair):
        childIndex = len(self.arr)
        self.arr.append(pair)
        parentIndex = self.parentIndex(childIndex)
        while self.inRange(childIndex) and self.inRange(parentIndex) and self.arr[childIndex][1] < self.arr[parentIndex][1]:
            self.arr[childIndex], self.arr[parentIndex] = self.arr[parentIndex], self.arr[childIndex]
            childIndex, parentIndex = parentIndex, self.parentIndex(parentIndex)
    def deleteMin(self):
        temp = self.arr[0]
        if len(self.arr) == 1:
            return temp
        self.arr[0] = self.arr.pop()
        currIndex = 0
        leftChildIndex = self.leftChildIndex(currIndex)
        rightChildIndex = self.rightChildIndex(currIndex)
        #while left child or right child is less than current, swap min child with current
        while self.inRange(leftChildIndex) + self.inRange(rightChildIndex):
            if not self.inRange(leftChildIndex):
                minChildIndex = rightChildIndex
            elif not self.inRange(rightChildIndex):
                minChildIndex = leftChildIndex
            else:
                if self.arr[rightChildIndex][1] < self.arr[leftChildIndex][1]:
                    minChildIndex = rightChildIndex
                else:
                    minChildIndex = leftChildIndex
            if self.arr[minChildIndex][1] < self.arr[currIndex][1]:
                self.arr[minChildIndex], self.arr[currIndex] = self.arr[currIndex], self.arr[minChildIndex]
                currIndex, leftChildIndex, rightChildIndex = minChildIndex, self.leftChildIndex(minChildIndex), self.rightChildIndex(minChildIndex)
            else:
                return temp
        return temp
    def incrementMin(self):
        pairs = [self.deleteMin()]
        while self.arr[0][1] == pairs[-1][1] or self.arr[0][1] == pairs[-1][1] + 1:
            pairs.append(self.deleteMin())
        for pair in pairs:
            temp = pair[1]
            while temp <= pairs[-1][1]:
                temp += pair[0]
            self.insert((pair[0], temp))
        return pairs[-1][1] + 1

class primes():
    def __init__(self):
        self.curr = 4
        self.primes = [2,3]
        self.minHeap = minHeap()
        self.minHeap.insert((2,4))
        self.minHeap.insert((3,9))
    def nextPrime(self):
        while self.curr == self.minHeap.arr[0][1]:
            self.curr = self.minHeap.incrementMin()
        self.primes.append(self.curr)
        self.minHeap.insert((self.curr, self.curr**2))
        self.curr += 1
    def primesLt(self, max):
        while self.primes[-1] < max:
            self.nextPrime()
    def isPrime(self, n):
        while self.primes[-1] < n:
            self.nextPrime()
        return n in self.primes
    def isComposite(self, n):
        return not self.isPrime(n)