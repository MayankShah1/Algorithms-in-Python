import circular_queue as CQ

def count_nodes(start):
    """Count the number of nodes in a circular linked list"""
    print('In function')
    print(start._element)
    walk = start._next
    count = 1
    while walk != start and walk is not None:
        print(walk._element)
        count += 1
        walk = walk._next
    return count

# Testing
if __name__ == "__main__":
    CL = CQ.CircularQueue()
    CL.enqueue(20)
    CL.enqueue(30)
    CL.enqueue(50)
    CL.dequeue()
    print(CL)
    print(count_nodes(CL.first()))
