# Queue implementation with enqueue, dequeue, and overflow / underflow error checking
# Chapter 10.1

class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        #initialize head and tail pointer to 0
        self.head = self.tail = 0
        self.is_full = False
        self.is_empty = True
        print("declare queue of size ",size)
    
    # input: x to insert into queue
    def enqueue(self,x):
        self.is_empty=False
        if self.is_full:
            print("error: queue overflow")
            return
        self.queue[self.tail]=x
        self.tail = (self.tail+1) % self.size
        if self.tail == self.head:
            self.is_full = True
        print("enqueue successful of ",x)
        
    # output: element removed from queue
    def dequeue(self):
        self.is_full = False
        if self.is_empty:
            print ("error: queue underflow")
            return
        x = self.queue[self.head]
        self.head = (self.head+1) % self.size
        if self.head==self.tail:
            self.is_empty=True
        print("dequeue ",x)
        return x

def main():
    Q = Queue(3)
    Q.enqueue(1)
    Q.enqueue(2)
    Q.enqueue(3)
    Q.enqueue(4)
    assert Q.dequeue() == 1
    assert Q.dequeue() == 2
    assert Q.dequeue() == 3
    Q.dequeue()
    Q.enqueue(1)
    Q.enqueue(2)
    Q.dequeue() == 1
    Q.enqueue(3)
    Q.enqueue(4)
    Q.enqueue(5)

if __name__=='__main__':
    main()

    
