def Selection_Sort(l,k):
    for i in range(0,k):
        minindex=i
        for j in range(i+1,k):
            if l[minindex]>l[j]:
                minindex=j
    l[i],l[minindex]=l[minindex],l[i]
    return(l[k-1])
