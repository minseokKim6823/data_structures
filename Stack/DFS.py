import Stack as st

def DFS():
    stack = st()
    stack.push((0,1))
    print("DFS:")

    while not stack.isEmpty():
        here =stack.pop()
        print(here,end='->')
        (x,y) =here
        if(map[y][x]=='x')

