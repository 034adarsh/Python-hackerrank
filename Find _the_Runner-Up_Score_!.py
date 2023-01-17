n = int(input())
lis = list(map(int, input().strip().split()))
x = max(lis)
while max(lis)==x:
    lis.remove(max(lis))
print(max(lis))

