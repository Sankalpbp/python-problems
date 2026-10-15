from collections import deque

deq = deque()

deq.append(1)
print(deq)
deq.append(2)
deq.append(3)

print(deq)

deq.popleft()
print(deq)
deq.pop()
print(deq)

deq.append(100)
deq.append(200)
deq.append(300)

print(deq)

deq.reverse()
print(deq)

