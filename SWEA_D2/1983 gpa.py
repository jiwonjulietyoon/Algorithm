# 1983. 조교의 성적 매기기


T = int(input())      # Number of Test Cases
for t in range(1, T+1):
    N, K = map(int, input().split())   
        # N : number of students (multiple of 10)
        # K : 학점을 알고 싶은 K번째 학생
    raw = []
    for n in range(N):
        mid, fin, hw = map(int, input().split())    # mid-term, finals, hw
        raw.append(mid * 0.35 + fin * 0.45 + hw * 0.2)
    
    rank = sorted(raw)[::-1].index(raw[K-1]) # ranking of target student
    num = int(N/10)                  # number of each letter grade

    gradelist = ["A+"] * num + ["A0"] * num + ["A-"] * num + ["B+"] * num + ["B0"] * num + ["B-"] * num + ["C+"] * num + ["C0"] * num + ["C-"] * num + ["D0"] * num
    
    print(f"#{t} {gradelist[rank]}")  # gradelist[rank] : target student's letter grade

