from itertools import combinations


def sigma_sum(arr):
    sigma = 0
    for i in range(len(arr)):
        sigma += (arr[i] * (i + 1))
    return sigma


def calculate_maximum_sum_possible(A, N):
    negatives = []
    positives = []
    for i in range(N):
        if A[i] < 0:
            negatives.append(A[i])
        else:
            positives.append(A[i])
    if len(negatives) == N:
        return 0
    if len(positives) == N:
        return sum(A)
    negative_possibilities = []
    sigma_list = []
    sigma_list.append(sigma_sum(A))
    for i in range(len(negatives)):
        negative_possibilities.append(combinations(negatives, i + 1))
    for comb in negative_possibilities:
        for tup in comb:
            B = A.copy()
            for value in tup:
                B.remove(value)
            sigma_list.append(sigma_sum(B))
    return max(sigma_list)


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    print(calculate_maximum_sum_possible(A, N))
