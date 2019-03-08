import sys
sys.stdin = open('../Input/tmp.txt', 'r')


C, R = map(int, input().split())  # C: 가로 -> W, R: 세로 -> H
K = int(input())

w, h = C-1, R
layers = [0, (w+h)*2-2]
w -= 2
h -= 2

while w > 0 and h > 0:
    tmp = layers[-1] + (w+h)*2-2
    # if tmp > K:
    #     break
    layers.append(tmp)
    w -= 2
    h -= 2

print(layers)


# K is in len(layers)th layer
# w += 2
# h += 2
# sub = [(w+h)*2-2, 2*w+h-1, w+h, w]
# for i in range(4):
#     if K < sub[i]:
#         break

#
# print(K-sub[i], i)
#
#
# print(layers)
# print(w, h)
# print(sub)
#
# # print(x, y)