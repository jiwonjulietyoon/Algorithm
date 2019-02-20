# -*- coding: utf-8 -*-
"""
Input: 빈 칸을 사이에 둔 두 개의 자연수 (1 ~ 9)
-> 사칙연산 + - * / 순서로 연산한 결과를 차례대로 출력한다
나누기에서 소수점 이하는 버린다.

예시: 
입력: 8 3

출력:
11
5
24
2
"""

a, b = [int(x) for x in input().split()]
print(a + b)
print(a - b)
print(a * b)
print(a // b)