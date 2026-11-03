def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    a, b = map(int, input().split())
    answer = gcd(a, b)
    print(answer)
