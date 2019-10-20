"""
Scissor: 1
Rock: 2
Paper: 3

input: A, B가 무엇을 냈는지 (빈 칸을 사이에 두고)
output: 이긴 사람 (no draws)

"""

A, B = [int(x) for x in input().split()]
if A == 1 and B == 3:
    winner = "A"
elif A == 3 and B == 1:
    winner = "B"
else:
    winner = "A" if A > B else "B"
print(winner)