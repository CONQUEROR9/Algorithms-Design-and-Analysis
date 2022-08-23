def insertion_sort(A):
    for j in range(1, A.__len__()):
        key = A[j]
        i = j-1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key

num = [999,24,566,243,3563,0,1,2,3,10,95,699,-100,-999,8]

insertion_sort(num)

print(num)
