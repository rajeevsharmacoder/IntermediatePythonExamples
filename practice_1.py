def function_fA(arr):
    sigma = 0
    n = len(arr)
    for i in range(n):
        sigma += ((i + 1) * arr[i])
    return sigma


def get_max_fA(A, N):
    buff = []
    buff.append(function_fA(A))
    negatives = [x for x in A if x < 0]
    if len(negatives) == 0:
        return buff[0]
    if len(negatives) == N:
        return 0
    print(buff)
    print(negatives)
    for i in range(0, len(negatives)):
        A.remove(negatives[i])
        print(A)
        fa = function_fA(A)
        print(fa)
        if fa > buff[-1]:
            buff.append(fa)
        print(buff)
    print(buff)
    return max(buff)


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        print(get_max_fA(A, N))
