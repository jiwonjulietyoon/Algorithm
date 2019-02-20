# 4676. 늘어지는 소리 만들기

for T in range(int(input())):
    word = list(input())
    _, hyp = input(), list(map(int, input().split()))
    for i in hyp:
        if i == 0:
            word[i] = "-" + word[i]
        else:
            word[i-1] += "-"
    print(f"#{T+1}", end=" ")
    print(*word, sep="")







############ 1st try ###############

for T in range(int(input())):
    word = list(input())
    L = len(word)
    for i in range(0, 2*L+1, 2):
        word.insert(i, "")
    
    _, hyp = input(), list(map(int, input().split()))
    for idx in hyp:
        word[2*idx] += "-"
    
    print(f"#{T+1}", end=" ")
    print(*word, sep="")
