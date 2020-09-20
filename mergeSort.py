
S = [4, 5, 1, 8, 3, 2, 7, 6,1,4,1,23,12,3,1,2,3,4,1,2,4,9,111,1]
def mergeSort(n,S):
    if ( n > 1) :
        h=n//2 #5,2,1
        m=n-h #5,3,1
        U = [0 for i in range(h)]
        V = [0 for i in range(m)]
        for i in range(h):
            U[i]=S[i]
        for i in range(h,n):
            V[i-h]=S[i]
        mergeSort(h,U)
        mergeSort(m,V)
        merge(h,m,U,V,S);

def merge (h,m,U,V,S):
    i=0;j=0;k=0;
    while (i<h and j<m):
        if(U[i] < V[j]):
            S[k]=U[i]
            i+=1
        else:
            S[k]=V[j]
            j+=1
        k+=1
    if(i>=h):
        for i in range(j,m):
            S[k]=V[i]
            k+=1
    else:
        for i in range(i,h):
            S[k]=U[i]
            k+=1
            
mergeSort(len(S),S)
print(S)
