# 5356 의석이의 세로로 말해요 


##### sb else's solution

for t in range(int(input())):
    array = [input() for _ in range(5)]
    l = max([ len(i) for i in array] )
     
    ans = ''
    for i in range(l):
        for j in range(5):
            try:
                ans += array[j][i]
            except:
                pass
 
    print(f'#{t+1} {ans}')








############
for T in range(int(input())):
    w = []
    for _ in range(5):
        w.append(list(input()))
    max_l = len(max(w, key=lambda x: len(x)))
    for x in w:
        while len(x) < max_l:
            x.append('')
    print(f"#{T+1}", end=" ")
    for i in range(max_l):
        for j in range(5):
            print(w[j][i], end="")
    print()