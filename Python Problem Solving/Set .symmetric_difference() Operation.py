n = int(input())
a = {}
b = {}
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))
x = a.symmetric_difference(b)
print(len(x))