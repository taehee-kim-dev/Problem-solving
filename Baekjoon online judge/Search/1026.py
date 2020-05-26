
# 1 <= N(자연수) <= 50
N = int(input())

# 0 <= A, B의 원소(정수) <= 100
A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))

A.sort()
B.sort(reverse=True)

answer = 0
for index in range(N):
    answer += A[index] * B[index]

print(answer)
