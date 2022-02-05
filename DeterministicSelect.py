# Select the ith smallest element in an array with n distinct elements with worst case O(n)
# Chapter 9.3

from math import ceil

def deterministicSelect(A,i):
    return helper(A,i,0,len(A)-1)

def helper(A,i,start,end):
    # If there is only one element in subarray, then return the element
    if end == start:
        return A[end]
    group = divideGroup(start,end)
    
    # For each group: insertion sort and find median
    medians = []
    for index in range(len(group)):
        insertionSort(group[index],A)
        medians.append(findMedian(group[index]))

    # Find median of medians and use it as pivot
    median = findMedian(medians)

    # Partition array with median as pivot
    x = partition(A,start,end,median)
    k = x+1

    if k == i:
        return A[x]
    if k > i:
        return helper(A,i,start,x-1)
    else:
        return helper(A,i,x+1,end)


# divid subarray into groups of 5 and last group with remaining n mod 5. Retrun indexes of elements in the groups
def divideGroup(start,end):
    num_ele = end-start+1
    num_group = ceil(num_ele/5)
    group = []
    group_start = start
    group_end = group_start+5
    for i in range(num_group-1):
        group.append(list(range(group_start,group_end)))
        group_start = group_end
        group_end = group_start+5
    group.append(list(range(group_start,end+1)))
    return group

# Helper to insertion sort groups, return array of indexes of sorted groups
def insertionSort(group,A):
    for i in range(len(group)):
        # element to insert
        x = A[group[i]]
        cur = i
        for j in range(i-1,-1,-1):
            if x < A[group[j]]:
                group[cur],group[j] = group[j],group[cur]
                cur -= 1
            else:
                break
# Helper to find median in a given list
def findMedian(A):
    length = len(A)
    if length % 2 == 0:
        return A[length//2-1]
    else:
        return A[length//2]

def partition(A,start,end,pivot):
    #put pivot to end of array
    A[pivot],A[end] = A[end],A[pivot]
    pivot_ele = A[end]
    i = start - 1
    for j in range(start,end):
        if A[j] <= pivot_ele:
            i += 1
            A[j],A[i] = A[i],A[j]
    A[i+1],A[end] = A[end],A[i+1]
    return i+1
def main():
    print("Test 1: ", [3,4,2,1,5,7,0,8,6,9], 7)
    print("returns: ", deterministicSelect([3,4,2,1,5,7,0,8,6,9],7), "should be: ", 6)
    print("Test 2",[3,1,2], 3)
    print("returns: ", deterministicSelect([3,1,2],3), "Should be: ", 3)
    print("Test 3",[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17], 4)
    print("returns: ", deterministicSelect([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],4), "should be: ", 4)

if __name__=="__main__":
    main()
