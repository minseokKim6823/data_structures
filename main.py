su,i=map(int,input().split())
i=(i-1)*2
list1=[]
def hanoi_tower(n,fr,tmp,to):
    if(n==1):
        if(su<=20):
            list1.append(fr)
            list1.append(to)
    else:
        hanoi_tower(n-1,fr,to,tmp)
        list1.append(fr)
        list1.append(to)
        hanoi_tower(n-1,tmp,fr,to)
        print(list1[i], end=" ")
        print(list1[i + 1])
hanoi_tower(su,1,2,3)

