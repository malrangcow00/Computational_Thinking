import sys
input = sys.stdin.readline

N = int(input().rstrip()[0:-1] + '00')
F = int(input())
while N % F != 0:
    N += 1
print(str(N)[-2:])