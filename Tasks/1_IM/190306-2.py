

# 4751. 다솔이의 다이아몬드 장식

for _ in range(int(input())):
    s = input()
    N = len(s)
    deco = [".", ".", "#", ".", "."]

    for i in range(N):
        deco[0] += ".#.."
        deco[1] += "#.#."
        deco[2] += ".{}.#".format(s[i])
        deco[3] += "#.#."
        deco[4] += ".#.."

    print(*deco, sep="\n")