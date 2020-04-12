def CountingSort(l):
    N=len(l)
    M=max(l)
    count=[0]*(M+1)
    count_sum=[0]*(M+1)
    for i in l:
        count[i]+=1
    count_sum[0]=count[0]
    for i in range(1,M+1):
        count_sum[i]=count_sum[i-1]+count[i]
    B=[0]*(N+1)
    for i in range(N-1,-1,-1):
        B[count_sum[l[i]]]=l[i]
        count_sum[l[i]]-=1
    print(B)
        
