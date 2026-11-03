def gcd(first: int, second: int) -> int:
    first, second = abs(first), abs(second)
    while second != 0:
        remainder = first % second
        first = second
        second = remainder
    return first


if __name__ == "__main__":
    first, second = map(int, input().split())
    answer = gcd(first, second)
    print(answer)
