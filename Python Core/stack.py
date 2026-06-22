string="""Stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) manner. In stack, a new element is added at one end and an element is removed from that end only. The insert and delete operations are often called push and pop. In Python, we can implement Stack using List Data Structure."""

print(string)

stack=list()

# inserting elements in a stack using list
stack.append("Mayank")
stack.append("Rajat")
stack.append("Kajal")
stack.append("Neha")
stack.append("Papamammi")

print(stack)
stack.pop()
stack.pop()

print(stack)