import timeit

quicksort_testcode = '''
def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i+1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r) '''

heapsort_testcode = '''
def parent(i):
    return i // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def Max_heapify(A, i, heap_size): #heap_size positional argument is taken to update heap_size from heapsort function
    l = left(i)
    r = right(i)
    if l < heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        Max_heapify(A, largest, heap_size)


def build_max_heap(A):
    heap_size = len(A)
    for i in range((heap_size // 2) - 1, -1, -1):
        Max_heapify(A, i, heap_size)


def Heapsort(A):
    build_max_heap(A)
    for i in range(len(A) - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        Max_heapify(A, 0, i)

'''

mergesort_testcode = '''
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
'''


def timetaken_10(A):
    total_time = timeit.repeat(stmt=A, number=10)
    return total_time


def timetaken_100(A):
    total_time = timeit.repeat(stmt=A, number=100)
    return total_time


def timetaken_1000(A):
    total_time = timeit.repeat(stmt=A, number=1000)
    return total_time

print("-------------------------------------------")

print("\tN = 10")

print("-------------------------------------------\n")

print("Time taken for quicksort : " + str(min(timetaken_10(quicksort_testcode))))

print("Time taken for mergesort : " + str(min(timetaken_10(mergesort_testcode))))

print("Time taken for heapsort : " + str(min(timetaken_10(heapsort_testcode))))

print("\n-------------------------------------------")

print("\tN = 100")

print("-------------------------------------------\n")

print("Time taken for quicksort : " + str(min(timetaken_100(quicksort_testcode))))

print("Time taken for mergesort : " + str(min(timetaken_100(mergesort_testcode))))

print("Time taken for heapsort : " + str(min(timetaken_100(heapsort_testcode))))

print("\n-------------------------------------------")

print("\tN = 1000")

print("-------------------------------------------\n")

print("Time taken for quicksort : " + str(min(timetaken_1000(quicksort_testcode))))

print("Time taken for mergesort : " + str(min(timetaken_1000(mergesort_testcode))))

print("Time taken for heapsort : " + str(min(timetaken_1000(heapsort_testcode))))

print("\n-------------------------------------------")
