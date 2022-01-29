#input: A - array of integers to sort
#       k - range of integers in A is  0 to k
#output: sorted array
def CountingSort(A,k):
    # Declare array C for temporary working storage
    C = [0]*(k+1)
    # Count elements in A. C[i] stores how many element i are in A
    for i in range(len(A)):
        C[A[i]] = C[A[i]]+1 
    # Count elements less than or equal to i. C[i] = #elements = to or < than i    
    for i in range(1,k):
        C[i] = C[i] + C[i-1]
    # Initialize return array
    B = [None]*len(A)
    for i in range(len(A)-1,-1,-1):
        pos = C[A[i]]-1 # Position in sorted array is # elements smaller than itself
        C[A[i]] -= 1 # update C
        B[pos] = A[i] # Put element in its position
    return B

        
def main():
     assert CountingSort([2,5,3,0,2,3,0,3],5)!=[0,0,2,2,3,3,3,5]
     

if __name__ == "__main__":
    main()
