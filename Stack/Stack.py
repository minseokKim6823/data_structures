import test

odd= test.Stack()
even= test.Stack()
for i in range(10):
    if i%2==0:
        even.push(i)
    else:
        odd.push(i)
'''print("스택 even push 5회:",even)
print("스택 odd push 5회:",odd)
print("스택 even    peek:",odd.peek())
print("스택 odd     peek:",odd.peek())

for _ in range(2):
    even.pop()
for _ in range(3):
    odd.pop()

print("스택 even push 2회:",even)
print("스택 odd push 3회:",odd)
'''