import queue
stack = queue.LifoQueue()
stack.put(2)
stack.put(3)
stack.put(7)
stack.put(4)
stack.put(1)
stack.put(9)
stack.put(8)

last_num = stack.get()        # Removes 8
second_last = stack.get()     # Removes 9

sum_last_two = last_num + second_last
print(f"Sum of last two ({last_num} + {second_last}): {sum_last_two}")

remaining_sum = 0

# FIX 2: Use .empty() or .qsize() because len() does not work on queues
while not stack.empty():
    remaining_sum += stack.get()

print(f"Sum of remaining elements: {remaining_sum}")