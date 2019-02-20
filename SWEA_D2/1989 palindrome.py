# 1989. 초심자의 회문 검사

T = int(input())
for t in range(T):
    word = input()
    res = 1 if word == word[::-1] else 0
    print(f"#{t+1} {res}")