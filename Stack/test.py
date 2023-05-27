import Stack as st

odd=st.Stack()
even=st.Stack()

for i in range(10):
    if i%2==0:
        even.push(i)
    else:
        odd.push(i)
print('스택 even push 5회:',even.t)
print('스택 odd push 5회:',odd.t)
print(odd)