def max_heapify(A, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < len(A) and A[left] > A[largest]:
        largest = left
    if right < len(A) and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)

def build_max_heap(A):
    for i in range(len(A) // 2, -1, -1):
        print i
        max_heapify(A, i)
    return A


A = range(9) 
print build_max_heap(A)

A1 = [2,4,1]
max_heap = build_max_heap(A1)

print '* * *'

def heap_sort(A, li=[]):
    A[0], A[-1] = A[-1], A[0]
    li.append(A.pop())
    try:
        max_heapify(A, A[0])
    except IndexError:
        return li
    return heap_sort(A, li=li)
    
print heap_sort(max_heap)
