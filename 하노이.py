su=int(input())
list1=[]
cnt=0
def hanoi_tower(n,fr,tmp,to):
    global cnt
    if(n==1):
        if(su<=20):
            list1.append(fr)
            list1.append(to)
            cnt+=1
        else:
            cnt += 1
    else:
        if (su <= 20):
            hanoi_tower(n-1,fr,to,tmp)
            list1.append(fr)
            list1.append(to)
            cnt += 1
            hanoi_tower(n-1,tmp,fr,to)
        else:
            hanoi_tower(n - 1, fr, to, tmp)
            cnt += 1
            hanoi_tower(n - 1, tmp, fr, to)
hanoi_tower(su,'1','2','3')
if(su>20):
    print(cnt)
for i in range(0,len(list1),2):
    if(su<=20):
        print(list1[i], end=" ")
        print(list1[i + 1])
