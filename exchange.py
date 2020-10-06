S=[4,5,1,9,10,8,3,2,7,6]
tmp=0

def exSort(S):
    count = 0
    for i in range(len(S)-1) :
        for j in range(i+1,len(S)) :
            if S[j] > S[i] :
                tmp=S[i]
                S[i]=S[j]
                S[j]=tmp
            print(S)
            count+=1
    print(count)
    
exSort(S)
