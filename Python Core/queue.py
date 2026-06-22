string="""Queue is a data structure that follows the First-In, First-Out (FIFO) principle, meaning the first element added is the first one to be removed. The insert and delete operations are often called enqueue and dequeue."""
print(string)

queue=list()

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
queue.append(6)
queue.append(7)
queue.append(8)

print(queue)

queue.pop(0)
queue.pop(0)
queue.pop(0)

print(queue)