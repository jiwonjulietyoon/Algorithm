
# n = int(input())  # first input
# p = sorted(list(map(int, input().split()))) # 2nd input
# print(p[round((len(p)-1)/2)])


N = int(input())
numbers = sorted(list(map(int, input().split())))
print(numbers[int((len(numbers)-1)/2)])