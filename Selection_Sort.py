def Selection_Sort(l,k):
    num=len(l)
    for i in range(0,num-1):
        minindex=i
        for j in range(i+1,num):
            if l[minindex]>l[j]:
                minindex=j
        l[i],l[minindex]=l[minindex],l[i]
    return(l[k-1])
