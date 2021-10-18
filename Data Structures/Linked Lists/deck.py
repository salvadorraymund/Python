from collections import deque

my_list = deque('abcde')
list1 = 'xyz'
my_list.append(list1)
print(my_list)

queue = deque()
customers = "Raymund", "Mela", "Dokie"
for c in customers:
    queue.append(c)
print(queue)
