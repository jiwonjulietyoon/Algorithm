"""
1 ~ 9999 사이의 자연수를 입력받아 각 자릿수의 합을 출력한다

예시: 6789 -> 30

"""


num = [int(x) for x in input()]
print(sum(num))