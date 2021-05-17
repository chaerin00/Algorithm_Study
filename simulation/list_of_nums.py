n,k=map(int,input().split())
if k<n:
    A=list(map(int,input().split(',')))
    A=A[:n]

    for num in range(k):
        B=[]
        for i in range(len(A)-1):
            B.append(A[i+1]-A[i])
        A=B
    print(B)
