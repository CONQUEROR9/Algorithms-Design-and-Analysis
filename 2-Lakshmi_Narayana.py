def merge(A, p, q, r):
    n1 = q-p+1
    n2 = r-q
    L = [None] * n1
    R = [None] * n2
    for i in range(0, n1):
        L[i] = A[p+i]
    for j in range(0, n2):
        R[j] = A[q+j+1]
    i = 0
    j = 0
    k = p
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i+1
        else:
            A[k] = R[j]
            j = j+1
        k = k+1
    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1

def mergesort(A, p, r):
    if p < r:
        q = (p+r)//2
        mergesort(A, p, q)
        mergesort(A, q+1, r)
        merge(A, p, q, r)

num = [999,24,566,243,3563,0,1,2,3,10,95,699,-100,-999,8]

mergesort(num, 0, num.__len__()-1)

print(num)
