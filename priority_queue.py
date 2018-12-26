from datastruct import PriorityMinQueue

if __name__ == '__main__':
    pq = PriorityMinQueue()
    pq.enqueue(1, 1)
    pq.enqueue(50, 50)
    pq.enqueue(10, '10-0')
    pq.enqueue(10, '10-1')
    pq.enqueue(15, 15)
    pass