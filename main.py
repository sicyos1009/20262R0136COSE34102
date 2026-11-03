a, b = map(int, input().split())
a, b = abs(a), abs(b)
while b:
    a, b = b, a % b
print(a)
