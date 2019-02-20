# 5215 Hamburger Diet




######## sb else's solution:
def linearSearch(cal,index):
    if index==N:
        return 0
    unpick=linearSearch(cal,index+1)
    pick=0
    if cal+foodList[index][1]<L:
        pick=linearSearch(cal+foodList[index][1],index+1)+foodList[index][0]
    return max(pick,unpick)
 
for t in range(int(input())):
    foodList=[]
    N,L=map(int,input().split())
    for i in range(N):
        foodList.append(list(map(int,input().split())))
    print(f"#{t+1} {linearSearch(0,0)}")





######### 2nd try ########

for T in range(int(input())):
    N, L = map(int, input().split())
    K = [list(map(int, input().split())) for _ in range(N)] # (score, calories)
    Max = 0
    for i in range(1, 1<<N):   # eliminate empty subset
        ss = cal = 0   # sum of scores in subset, sum of calories in subset
        for j in range(N):
            if i & (1<<j):
                ss += K[j][0]
                cal += K[j][1]
        if cal <= L:
            if ss > Max:
                Max = ss
    print(f"#{T+1} {Max}")






######### 1st try ########

for T in range(int(input())):
    N, L = map(int, input().split())
    K = [list(map(int, input().split())) for _ in range(N)] # (score, calories)
    
    subset = [] # compilation of subsets that meet the calories limit
    for i in range(1, 1<<N):   # eliminate empty subset
        ss = cal = 0   # sum of scores in subset, sum of calories in subset
        for j in range(N):
            if i & (1<<j):
                ss += K[j][0]
                cal += K[j][1]
        if cal <= L:
            subset.append(ss)
    print(f"#{T+1} {max(subset)}")