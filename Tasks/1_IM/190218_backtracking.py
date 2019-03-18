
# 문제: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 의 부분집합 중 합이 10인 것만 출력하기






########################## 접근 1 #########################
####### powerset 구하기 + subset의 합이 10인 것만 출력하기 ###

def process_solution(a, k):
    Sum = 0
    for i in range(1, 11):
        if a[i] == True:
            Sum += i
    if Sum == 10:              # subset 합이 10일 때
        for i in range(1, 11):
            if a[i] == True:
                print(i, end=" ")
        print()

def construct_candidates(a, k, Input, c):
    c[0] = True
    c[1] = False
    return 2

def backtrack(a, k, Input):
    global cnt
    cnt += 1
    c = [0] * 100
    if k == Input:
        process_solution(a, k)     # 10단계를 다 거쳐야만 각각의 부분집합의 합을 구하기 시작한다.
    else:
        k += 1
        ncandidates = construct_candidates(a, k, Input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, Input)


a = [0] * 100
cnt = 0
backtrack(a, 0, 10)
print(cnt)       # 위 과정에서 backtracking 함수가 총 몇 번 불렸는지 count하기 (=> 2047)



##################### 접근 2 #############################

# 위 알고리즘에서 가지치기를 적용한다면?

def backtrack(a, k, Sum):
    global cnt
    cnt += 1
    if k == N:
        if Sum == 10:
            for i in range(1, 11):
                if a[i] == True:
                    print(i, end=" ")
            print()
    else:
        k += 1
        if Sum + k <= 10:        # 가지치지: 다음 단계로 내려갈지 말지 결정하기
            a[k] = 1
            backtrack(a, k, Sum+k)
        # a[k] = 1;
        # backtrack(a, k, Sum+k)
        a[k] = 0
        backtrack(a, k, Sum)

N = 10
a = [0] * 100

cnt = 0
backtrack(a, 0, 0)
print("cnt:", cnt)