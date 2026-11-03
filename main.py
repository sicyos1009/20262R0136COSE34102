def gcd(first, second):
    first, second = abs(first), abs(second)
    while second != 0:
        first, second = second, first % second
    return first


if __name__ == "__main__":
    first, second = map(int, input().split())
    answer = gcd(first, second)
    print(answer)
