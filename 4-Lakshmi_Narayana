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


A = [5, 3, 17, 10, 84, 19, 6, 22, 9]

Heapsort(A)

print(A)
