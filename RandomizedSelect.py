import random

#inputs: A - array
#        i - ith smallest 
#Output: ith smallest element of A
def RandomizedSelect(A,i): 
    return helper(A,0,len(A)-1,i)

#inputs: A - array
#        start - start index
#        end - end index
#        i - ith smallest element to return
#output: ith smallest element of A
def helper(A,start,end,i):
    #Base case
    if end == start:
        return A[end]
    pivot = randomizedPartition(A,start,end)
    if pivot+1 == i:
        return A[pivot]
    if pivot+1 > i:
        # partition left subarray
        return helper(A,start,pivot-1,i)
    else:
        #partition right subarray
        return helper(A,pivot+1,end,i)

#return pivot position after partitioning and partition the sub array 
def randomizedPartition(A,start,end):
    i = random.randint(start, end)
    #put pivot to end of array
    A[i],A[end] = A[end],A[i]
    pivot_ele = A[end]
    i = start - 1
    for j in range(start,end):
        if A[j] <= pivot_ele:
            i += 1
            A[j],A[i] = A[i],A[j]
    A[i+1],A[end] = A[end],A[i+1]
    return i+1

def main():
    assert RandomizedSelect([3,2,9,0,7,5,4,8,6,1],3)==2
    assert RandomizedSelect([1,0,0,2,2,1],3)==1
    print("Complete")

if __name__ == "__main__":
    main()
