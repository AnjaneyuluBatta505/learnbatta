def insertionsort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while(j >= 0 and key < A[j]):
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key

if __name__ == "__main__":
    A = [3, 2, 1, 4, 5]
    insertionsort(A)
    print(A)
