

def solution(A):
    for j in range(0, len(A)):
        A[j] = int(A[j])
        if A[j] < 0:
            A.pop(A[j])
solution([-1, -3, 1, 3])
